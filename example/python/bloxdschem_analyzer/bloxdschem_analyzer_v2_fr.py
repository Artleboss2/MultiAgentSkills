#!/usr/bin/env python3
"""
Enhanced Bloxd Schematic Analyzer
Supports multiple schematic formats and provides detailed analysis
"""

import struct
import gzip
import zlib
import io
import json
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any, Optional
import sys
import os

class NBTReader:
    """Enhanced NBT (Named Binary Tag) reader"""
    
    TAG_END = 0
    TAG_BYTE = 1
    TAG_SHORT = 2
    TAG_INT = 3
    TAG_LONG = 4
    TAG_FLOAT = 5
    TAG_DOUBLE = 6
    TAG_BYTE_ARRAY = 7
    TAG_STRING = 8
    TAG_LIST = 9
    TAG_COMPOUND = 10
    TAG_INT_ARRAY = 11
    TAG_LONG_ARRAY = 12
    
    def __init__(self, data: bytes):
        self.stream = io.BytesIO(data)
    
    def read_tag(self) -> Tuple[int, Optional[str], Any]:
        """Read a complete NBT tag"""
        tag_type = self.read_byte()
        
        if tag_type == self.TAG_END:
            return tag_type, None, None
        
        name = self.read_string()
        payload = self.read_payload(tag_type)
        
        return tag_type, name, payload
    
    def read_byte(self) -> int:
        return struct.unpack('b', self.stream.read(1))[0]
    
    def read_unsigned_byte(self) -> int:
        return struct.unpack('B', self.stream.read(1))[0]
    
    def read_short(self) -> int:
        return struct.unpack('>h', self.stream.read(2))[0]
    
    def read_int(self) -> int:
        return struct.unpack('>i', self.stream.read(4))[0]
    
    def read_long(self) -> int:
        return struct.unpack('>q', self.stream.read(8))[0]
    
    def read_float(self) -> float:
        return struct.unpack('>f', self.stream.read(4))[0]
    
    def read_double(self) -> float:
        return struct.unpack('>d', self.stream.read(8))[0]
    
    def read_string(self) -> str:
        length = struct.unpack('>H', self.stream.read(2))[0]
        if length == 0:
            return ""
        return self.stream.read(length).decode('utf-8', errors='ignore')
    
    def read_byte_array(self) -> List[int]:
        length = self.read_int()
        return [self.read_byte() for _ in range(length)]
    
    def read_int_array(self) -> List[int]:
        length = self.read_int()
        return [self.read_int() for _ in range(length)]
    
    def read_list(self) -> List[Any]:
        tag_type = self.read_unsigned_byte()
        length = self.read_int()
        return [self.read_payload(tag_type) for _ in range(length)]
    
    def read_compound(self) -> Dict[str, Any]:
        compound = {}
        while True:
            tag_type, name, payload = self.read_tag()
            if tag_type == self.TAG_END:
                break
            compound[name] = payload
        return compound
    
    def read_payload(self, tag_type: int) -> Any:
        if tag_type == self.TAG_BYTE:
            return self.read_byte()
        elif tag_type == self.TAG_SHORT:
            return self.read_short()
        elif tag_type == self.TAG_INT:
            return self.read_int()
        elif tag_type == self.TAG_LONG:
            return self.read_long()
        elif tag_type == self.TAG_FLOAT:
            return self.read_float()
        elif tag_type == self.TAG_DOUBLE:
            return self.read_double()
        elif tag_type == self.TAG_BYTE_ARRAY:
            return self.read_byte_array()
        elif tag_type == self.TAG_STRING:
            return self.read_string()
        elif tag_type == self.TAG_LIST:
            return self.read_list()
        elif tag_type == self.TAG_COMPOUND:
            return self.read_compound()
        elif tag_type == self.TAG_INT_ARRAY:
            return self.read_int_array()
        else:
            return None

class BloxdSchematicAnalyzer:
    """Analyzer for Bloxd schematic files"""
    
    # Extended Minecraft/Bloxd block database
    BLOCK_DATABASE = {
        0: {"name": "Air", "category": "Utility"},
        1: {"name": "Stone", "category": "Building"},
        2: {"name": "Grass Block", "category": "Nature"},
        3: {"name": "Dirt", "category": "Nature"},
        4: {"name": "Cobblestone", "category": "Building"},
        5: {"name": "Oak Planks", "category": "Building"},
        6: {"name": "Sapling", "category": "Nature"},
        7: {"name": "Bedrock", "category": "Utility"},
        8: {"name": "Water", "category": "Liquid"},
        9: {"name": "Stationary Water", "category": "Liquid"},
        10: {"name": "Lava", "category": "Liquid"},
        11: {"name": "Stationary Lava", "category": "Liquid"},
        12: {"name": "Sand", "category": "Nature"},
        13: {"name": "Gravel", "category": "Nature"},
        14: {"name": "Gold Ore", "category": "Ore"},
        15: {"name": "Iron Ore", "category": "Ore"},
        16: {"name": "Coal Ore", "category": "Ore"},
        17: {"name": "Oak Log", "category": "Nature"},
        18: {"name": "Oak Leaves", "category": "Nature"},
        19: {"name": "Sponge", "category": "Utility"},
        20: {"name": "Glass", "category": "Building"},
        21: {"name": "Lapis Ore", "category": "Ore"},
        22: {"name": "Lapis Block", "category": "Building"},
        23: {"name": "Dispenser", "category": "Redstone"},
        24: {"name": "Sandstone", "category": "Building"},
        25: {"name": "Note Block", "category": "Redstone"},
        35: {"name": "Wool", "category": "Building"},
        41: {"name": "Gold Block", "category": "Building"},
        42: {"name": "Iron Block", "category": "Building"},
        43: {"name": "Double Stone Slab", "category": "Building"},
        44: {"name": "Stone Slab", "category": "Building"},
        45: {"name": "Bricks", "category": "Building"},
        46: {"name": "TNT", "category": "Utility"},
        47: {"name": "Bookshelf", "category": "Decoration"},
        48: {"name": "Mossy Cobblestone", "category": "Building"},
        49: {"name": "Obsidian", "category": "Building"},
        50: {"name": "Torch", "category": "Decoration"},
        53: {"name": "Oak Stairs", "category": "Building"},
        54: {"name": "Chest", "category": "Utility"},
        56: {"name": "Diamond Ore", "category": "Ore"},
        57: {"name": "Diamond Block", "category": "Building"},
        58: {"name": "Crafting Table", "category": "Utility"},
        60: {"name": "Farmland", "category": "Nature"},
        61: {"name": "Furnace", "category": "Utility"},
        64: {"name": "Oak Door", "category": "Utility"},
        65: {"name": "Ladder", "category": "Utility"},
        67: {"name": "Cobblestone Stairs", "category": "Building"},
        73: {"name": "Redstone Ore", "category": "Ore"},
        79: {"name": "Ice", "category": "Nature"},
        80: {"name": "Snow Block", "category": "Nature"},
        81: {"name": "Cactus", "category": "Nature"},
        82: {"name": "Clay", "category": "Nature"},
        83: {"name": "Sugar Cane", "category": "Nature"},
        85: {"name": "Oak Fence", "category": "Building"},
        89: {"name": "Glowstone", "category": "Building"},
        98: {"name": "Stone Bricks", "category": "Building"},
        99: {"name": "Brown Mushroom Block", "category": "Nature"},
        100: {"name": "Red Mushroom Block", "category": "Nature"},
        101: {"name": "Iron Bars", "category": "Building"},
        102: {"name": "Glass Pane", "category": "Building"},
        103: {"name": "Melon", "category": "Nature"},
        109: {"name": "Stone Brick Stairs", "category": "Building"},
        121: {"name": "End Stone", "category": "Building"},
        155: {"name": "Quartz Block", "category": "Building"},
        159: {"name": "Stained Clay", "category": "Building"},
        164: {"name": "Acacia Stairs", "category": "Building"},
        172: {"name": "Hardened Clay", "category": "Building"},
        174: {"name": "Packed Ice", "category": "Nature"},
    }
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.width = 0
        self.height = 0
        self.length = 0
        self.offset_x = 0
        self.offset_y = 0
        self.offset_z = 0
        self.block_counts = Counter()
        self.metadata = {}
    
    def decompress_data(self, data: bytes) -> bytes:
        """Try to decompress the data"""
        # Try gzip
        if data[:2] == b'\x1f\x8b':
            try:
                return gzip.decompress(data)
            except:
                pass
        
        # Try zlib
        try:
            return zlib.decompress(data)
        except:
            pass
        
        # Try zlib with different windowbits
        try:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except:
            pass
        
        return data
    
    def parse_nbt(self, data: bytes) -> Optional[Dict]:
        """Parse NBT data"""
        try:
            reader = NBTReader(data)
            tag_type, name, payload = reader.read_tag()
            return payload if isinstance(payload, dict) else None
        except Exception as e:
            print(f"⚠️  NBT parsing error: {e}")
            return None
    
    def analyze_file(self):
        """Main analysis function"""
        print(f"\n{'='*70}")
        print(f"📂 BLOXD SCHEMATIC ANALYZER")
        print(f"{'='*70}")
        print(f"File: {os.path.basename(self.filepath)}")
        print(f"Path: {self.filepath}")
        
        # Read file
        try:
            with open(self.filepath, 'rb') as f:
                raw_data = f.read()
            print(f"Size: {len(raw_data):,} bytes ({len(raw_data)/1024:.2f} KB)")
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return
        
        # Decompress
        data = self.decompress_data(raw_data)
        if len(data) != len(raw_data):
            print(f"🗜️  Decompressed to: {len(data):,} bytes ({len(data)/1024:.2f} KB)")
        
        # Parse NBT
        nbt_data = self.parse_nbt(data)
        
        if nbt_data:
            self.parse_schematic_nbt(nbt_data)
        else:
            print("⚠️  Could not parse as NBT, attempting raw analysis...")
            self.parse_raw_blocks(data)
        
        self.display_results()
    
    def parse_schematic_nbt(self, nbt: Dict):
        """Parse schematic from NBT data"""
        print("\n📊 NBT Structure detected!")
        
        # Extract dimensions
        self.width = nbt.get('Width', nbt.get('width', 0))
        self.height = nbt.get('Height', nbt.get('height', 0))
        self.length = nbt.get('Length', nbt.get('length', 0))
        
        # Extract offsets
        self.offset_x = nbt.get('WEOffsetX', 0)
        self.offset_y = nbt.get('WEOffsetY', 0)
        self.offset_z = nbt.get('WEOffsetZ', 0)
        
        # Extract metadata
        self.metadata['Materials'] = nbt.get('Materials', 'Unknown')
        
        # Extract blocks
        blocks = nbt.get('Blocks', [])
        if blocks:
            for block_id in blocks:
                self.block_counts[block_id] += 1
        
        # Try AddBlocks for extended IDs
        add_blocks = nbt.get('AddBlocks', [])
        if add_blocks:
            print("📦 Extended block IDs detected")
    
    def parse_raw_blocks(self, data: bytes):
        """Parse blocks from raw data"""
        print("\n🔍 Performing raw byte analysis...")
        
        # Count all bytes as potential block IDs
        for byte in data:
            if 0 <= byte <= 200:  # Reasonable block ID range
                self.block_counts[byte] += 1
        
        # Estimate dimensions from data size
        total = sum(self.block_counts.values())
        if total > 0:
            # Try to guess cubic dimensions
            side = round(total ** (1/3))
            self.width = side
            self.height = side
            self.length = side
    
    def display_results(self):
        """Display analysis results"""
        print(f"\n{'='*70}")
        print("📐 DIMENSIONS")
        print(f"{'='*70}")
        print(f"Width  (X): {self.width}")
        print(f"Height (Y): {self.height}")
        print(f"Length (Z): {self.length}")
        print(f"Volume: {self.width * self.height * self.length:,} blocks")
        
        if self.offset_x or self.offset_y or self.offset_z:
            print(f"\nOffset: ({self.offset_x}, {self.offset_y}, {self.offset_z})")
        
        if not self.block_counts:
            print("\n❌ No blocks found!")
            return
        
        # Calculate statistics
        total_blocks = sum(self.block_counts.values())
        unique_types = len(self.block_counts)
        
        print(f"\n{'='*70}")
        print("📊 STATISTICS")
        print(f"{'='*70}")
        print(f"Total blocks: {total_blocks:,}")
        print(f"Unique types: {unique_types}")
        
        # Group by category
        categories = defaultdict(int)
        for block_id, count in self.block_counts.items():
            category = self.BLOCK_DATABASE.get(block_id, {}).get('category', 'Unknown')
            categories[category] += count
        
        print(f"\n{'='*70}")
        print("🏷️  BLOCKS BY CATEGORY")
        print(f"{'='*70}")
        for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_blocks) * 100
            print(f"{category:15} {count:8,} ({percentage:5.1f}%)")
        
        # Detailed block list
        print(f"\n{'='*70}")
        print("🧱 DETAILED BLOCK COUNT")
        print(f"{'='*70}")
        print(f"{'Block Name':<30} {'ID':>4}  {'Count':>10}  {'%':>6}  {'Bar'}")
        print(f"{'-'*70}")
        
        sorted_blocks = sorted(self.block_counts.items(), key=lambda x: x[1], reverse=True)
        
        for block_id, count in sorted_blocks[:50]:  # Top 50
            block_info = self.BLOCK_DATABASE.get(block_id, {"name": f"Unknown ({block_id})", "category": "Unknown"})
            block_name = block_info['name']
            percentage = (count / total_blocks) * 100
            
            # Progress bar
            bar_length = int(percentage / 2)
            bar = "█" * min(bar_length, 30)
            
            print(f"{block_name:<30} {block_id:>4}  {count:>10,}  {percentage:>5.1f}% {bar}")
        
        if len(sorted_blocks) > 50:
            print(f"\n... and {len(sorted_blocks) - 50} more block types")
        
        # Top 10 summary
        print(f"\n{'='*70}")
        print("🏆 TOP 10 BLOCKS")
        print(f"{'='*70}")
        for i, (block_id, count) in enumerate(sorted_blocks[:10], 1):
            block_info = self.BLOCK_DATABASE.get(block_id, {"name": f"Unknown ({block_id})"})
            percentage = (count / total_blocks) * 100
            print(f"{i:2}. {block_info['name']:<25} {count:>10,} ({percentage:5.1f}%)")
        
        print(f"\n{'='*70}\n")

def main():
    if len(sys.argv) < 2:
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║           BLOXD SCHEMATIC ANALYZER v2.0                      ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print()
        print("Usage:")
        print("  python bloxdschem_analyzer.py <file.bloxdschem>")
        print()
        print("Example:")
        print("  python bloxdschem_analyzer.py jesusschem.bloxdschem")
        print()
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found!")
        sys.exit(1)
    
    analyzer = BloxdSchematicAnalyzer(filepath)
    analyzer.analyze_file()

if __name__ == "__main__":
    main()