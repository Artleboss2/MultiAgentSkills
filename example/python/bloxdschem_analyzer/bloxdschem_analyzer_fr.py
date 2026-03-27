#!/usr/bin/env python3
"""
Bloxd Schematic (.bloxdschem) Analyzer
Reads and analyzes .bloxdschem files to count block types
"""

import struct
import gzip
import io
from collections import Counter
from typing import Dict, Tuple, Any
import sys

class BloxdSchemReader:
    """Reader for .bloxdschem files (Minecraft-like schematic format)"""
    
    # Common Minecraft block IDs (peut être adapté pour Bloxd)
    BLOCK_NAMES = {
        0: "Air",
        1: "Stone",
        2: "Grass Block",
        3: "Dirt",
        4: "Cobblestone",
        5: "Oak Planks",
        7: "Bedrock",
        8: "Water",
        9: "Stationary Water",
        10: "Lava",
        11: "Stationary Lava",
        12: "Sand",
        13: "Gravel",
        14: "Gold Ore",
        15: "Iron Ore",
        16: "Coal Ore",
        17: "Oak Log",
        18: "Oak Leaves",
        20: "Glass",
        24: "Sandstone",
        35: "Wool",
        41: "Gold Block",
        42: "Iron Block",
        43: "Double Stone Slab",
        44: "Stone Slab",
        45: "Bricks",
        46: "TNT",
        47: "Bookshelf",
        48: "Mossy Cobblestone",
        49: "Obsidian",
        50: "Torch",
        53: "Oak Stairs",
        54: "Chest",
        56: "Diamond Ore",
        57: "Diamond Block",
        58: "Crafting Table",
        60: "Farmland",
        61: "Furnace",
        62: "Burning Furnace",
        64: "Oak Door",
        65: "Ladder",
        67: "Cobblestone Stairs",
        73: "Redstone Ore",
        79: "Ice",
        80: "Snow Block",
        81: "Cactus",
        82: "Clay",
        83: "Sugar Cane",
        85: "Oak Fence",
        89: "Glowstone",
        98: "Stone Bricks",
        99: "Brown Mushroom Block",
        100: "Red Mushroom Block",
        101: "Iron Bars",
        102: "Glass Pane",
        103: "Melon",
        109: "Stone Brick Stairs",
        121: "End Stone",
        155: "Quartz Block",
        159: "Stained Clay",
        164: "Acacia Stairs",
        172: "Hardened Clay",
        174: "Packed Ice",
    }
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None
        self.width = 0
        self.height = 0
        self.length = 0
        self.blocks = []
        self.block_data = []
        
    def read_file(self) -> bytes:
        """Read the schematic file"""
        try:
            with open(self.filepath, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            sys.exit(1)
    
    def try_decompress(self, data: bytes) -> bytes:
        """Try to decompress if the file is gzipped"""
        # Check for gzip magic number
        if data[:2] == b'\x1f\x8b':
            try:
                return gzip.decompress(data)
            except:
                pass
        
        # Try zlib decompress
        try:
            import zlib
            return zlib.decompress(data)
        except:
            pass
        
        return data
    
    def read_nbt_tag(self, stream: io.BytesIO) -> Tuple[int, Any]:
        """Read an NBT tag (simplified NBT parser)"""
        try:
            tag_type = struct.unpack('B', stream.read(1))[0]
            
            if tag_type == 0:  # TAG_End
                return 0, None
            
            # Read name length and name
            name_length = struct.unpack('>H', stream.read(2))[0]
            name = stream.read(name_length).decode('utf-8') if name_length > 0 else ""
            
            # Read payload based on type
            if tag_type == 1:  # TAG_Byte
                value = struct.unpack('b', stream.read(1))[0]
            elif tag_type == 2:  # TAG_Short
                value = struct.unpack('>h', stream.read(2))[0]
            elif tag_type == 3:  # TAG_Int
                value = struct.unpack('>i', stream.read(4))[0]
            elif tag_type == 7:  # TAG_Byte_Array
                length = struct.unpack('>i', stream.read(4))[0]
                value = list(struct.unpack(f'{length}b', stream.read(length)))
            elif tag_type == 8:  # TAG_String
                length = struct.unpack('>H', stream.read(2))[0]
                value = stream.read(length).decode('utf-8')
            elif tag_type == 10:  # TAG_Compound
                value = {}
                while True:
                    child_type, child_value = self.read_nbt_tag(stream)
                    if child_type == 0:
                        break
                    if isinstance(child_value, tuple) and len(child_value) == 2:
                        value[child_value[0]] = child_value[1]
            else:
                value = None
            
            return tag_type, (name, value)
        except Exception as e:
            return 0, None
    
    def parse_schematic_data(self, data: bytes) -> Dict[str, int]:
        """Parse schematic data and count blocks"""
        # Try to decompress first
        decompressed = self.try_decompress(data)
        
        block_counter = Counter()
        
        # Method 1: Try NBT parsing
        try:
            stream = io.BytesIO(decompressed)
            tag_type, root = self.read_nbt_tag(stream)
            
            if root and isinstance(root, tuple) and len(root) == 2:
                name, compound = root
                if isinstance(compound, dict):
                    # Extract dimensions
                    self.width = compound.get('Width', 0)
                    self.height = compound.get('Height', 0)
                    self.length = compound.get('Length', 0)
                    
                    print(f"📐 Dimensions: {self.width} x {self.height} x {self.length}")
                    print(f"📦 Total volume: {self.width * self.height * self.length} blocks")
                    print()
                    
                    # Get blocks array
                    blocks = compound.get('Blocks', [])
                    if blocks:
                        for block_id in blocks:
                            if isinstance(block_id, int):
                                block_counter[block_id] += 1
                        
                        if block_counter:
                            return block_counter
        except Exception as e:
            print(f"⚠️  NBT parsing failed: {e}")
        
        # Method 2: Raw byte analysis
        print("🔍 Attempting raw byte analysis...")
        
        # Look for patterns in the data
        for i in range(len(decompressed)):
            byte_val = decompressed[i]
            # Most block IDs are in range 0-200
            if 0 <= byte_val <= 200:
                block_counter[byte_val] += 1
        
        # Filter out unlikely blocks (too many occurrences suggest it's not block data)
        total = sum(block_counter.values())
        filtered_counter = Counter()
        for block_id, count in block_counter.items():
            # Keep blocks that appear reasonable amount
            if count < total * 0.3:  # Not more than 30% of total
                filtered_counter[block_id] = count
        
        return filtered_counter if filtered_counter else block_counter
    
    def analyze(self):
        """Main analysis function"""
        print(f"📂 Reading file: {self.filepath}")
        print("=" * 60)
        
        data = self.read_file()
        print(f"📊 File size: {len(data)} bytes")
        
        # Check if compressed
        if data[:2] == b'\x1f\x8b':
            print("🗜️  File is gzip compressed")
        
        print()
        
        block_counts = self.parse_schematic_data(data)
        
        if not block_counts:
            print("❌ Could not parse block data")
            return
        
        # Sort by count (descending)
        sorted_blocks = sorted(block_counts.items(), key=lambda x: x[1], reverse=True)
        
        print("🧱 BLOCK ANALYSIS:")
        print("=" * 60)
        
        total_blocks = sum(block_counts.values())
        
        for block_id, count in sorted_blocks:
            block_name = self.BLOCK_NAMES.get(block_id, f"Unknown Block {block_id}")
            percentage = (count / total_blocks) * 100
            
            # Create a simple bar chart
            bar_length = int(percentage / 2)  # Scale down for display
            bar = "█" * bar_length
            
            print(f"{block_name:25} (ID: {block_id:3}) | {count:6} | {percentage:5.1f}% {bar}")
        
        print("=" * 60)
        print(f"Total blocks counted: {total_blocks}")
        print(f"Unique block types: {len(block_counts)}")
        
        # Top 5 summary
        print()
        print("🏆 TOP 5 BLOCKS:")
        for i, (block_id, count) in enumerate(sorted_blocks[:5], 1):
            block_name = self.BLOCK_NAMES.get(block_id, f"Unknown Block {block_id}")
            print(f"  {i}. {block_name}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python bloxdschem_analyzer.py <file.bloxdschem>")
        print()
        print("Example:")
        print("  python bloxdschem_analyzer.py jesusschem.bloxdschem")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    analyzer = BloxdSchemReader(filepath)
    analyzer.analyze()

if __name__ == "__main__":
    main()