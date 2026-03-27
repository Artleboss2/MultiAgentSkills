#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terminal Graphique Windows - Version Avancée
Avec panneau de paramètres moderne, effet Glass avancé et design élégant
"""

import tkinter as tk
from tkinter import scrolledtext, colorchooser, filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
import os
import sys
import subprocess
import threading
from datetime import datetime
import json
from pathlib import Path
import platform
import ctypes

class ModernButton(tk.Canvas):
    """Bouton moderne avec effet hover"""
    
    def __init__(self, parent, text, command, bg="#007ACC", fg="white", hover_bg="#005A9E", **kwargs):
        super().__init__(parent, highlightthickness=0, **kwargs)
        self.text = text
        self.command = command
        self.bg = bg
        self.fg = fg
        self.hover_bg = hover_bg
        self.is_hovered = False
        
        self.config(bg=bg, width=120, height=35)
        self.text_id = self.create_text(60, 17, text=text, fill=fg, font=("Segoe UI", 10, "bold"))
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        
    def on_enter(self, e):
        self.config(bg=self.hover_bg)
        self.is_hovered = True
        
    def on_leave(self, e):
        self.config(bg=self.bg)
        self.is_hovered = False
        
    def on_click(self, e):
        if self.command:
            self.command()

class SettingsPanel:
    """Panneau de paramètres moderne du terminal"""
    
    def __init__(self, parent, terminal):
        self.parent = parent
        self.terminal = terminal
        self.window = None
        
    def show(self):
        """Affiche le panneau de paramètres"""
        if self.window and self.window.winfo_exists():
            self.window.lift()
            return
        
        self.window = tk.Toplevel(self.parent)
        self.window.title("⚙️ Paramètres du Terminal")
        self.window.geometry("800x750")
        self.window.configure(bg="#1E1E1E")
        
        # Style moderne pour ttk
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style pour Notebook
        style.configure("TNotebook", background="#1E1E1E", borderwidth=0)
        style.configure("TNotebook.Tab", 
                       background="#2D2D30", 
                       foreground="white",
                       padding=[20, 10],
                       font=("Segoe UI", 10))
        style.map("TNotebook.Tab",
                 background=[("selected", "#007ACC")],
                 foreground=[("selected", "white")])
        
        # En-tête moderne
        header = tk.Frame(self.window, bg="#007ACC", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        header_title = tk.Label(
            header,
            text="⚙️  Paramètres du Terminal",
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )
        header_title.pack(side=tk.LEFT, padx=20, pady=15)
        
        # Notebook (onglets)
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Onglet Apparence
        appearance_frame = tk.Frame(notebook, bg="#1E1E1E")
        notebook.add(appearance_frame, text="🎨  Apparence")
        self.create_appearance_tab(appearance_frame)
        
        # Onglet Transparence
        transparency_frame = tk.Frame(notebook, bg="#1E1E1E")
        notebook.add(transparency_frame, text="💎  Effet Glass")
        self.create_transparency_tab(transparency_frame)
        
        # Onglet Image de Fond
        background_frame = tk.Frame(notebook, bg="#1E1E1E")
        notebook.add(background_frame, text="🖼️  Fond d'écran")
        self.create_background_tab(background_frame)
        
        # Onglet Commandes Personnalisées
        commands_frame = tk.Frame(notebook, bg="#1E1E1E")
        notebook.add(commands_frame, text="⚡  Commandes")
        self.create_commands_tab(commands_frame)
        
        # Onglet Alias
        alias_frame = tk.Frame(notebook, bg="#1E1E1E")
        notebook.add(alias_frame, text="🔗  Alias")
        self.create_alias_tab(alias_frame)
        
        # Footer avec boutons modernes
        footer = tk.Frame(self.window, bg="#252526", height=70)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)
        
        button_container = tk.Frame(footer, bg="#252526")
        button_container.pack(side=tk.RIGHT, padx=20, pady=15)
        
        save_btn = tk.Button(
            button_container,
            text="💾  Sauvegarder",
            command=self.save_settings,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            padx=25,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#005A9E",
            activeforeground="white"
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(
            button_container,
            text="❌  Annuler",
            command=self.window.destroy,
            bg="#3E3E42",
            fg="white",
            font=("Segoe UI", 11),
            padx=25,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#2D2D30",
            activeforeground="white"
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)
    
    def create_transparency_tab(self, parent):
        """Crée l'onglet de transparence/effet glass"""
        # Scroll frame
        canvas = tk.Canvas(parent, bg="#1E1E1E", highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1E1E1E")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        container = scrollable_frame
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # En-tête section
        title = tk.Label(
            container,
            text="💎  Effet Glass - Transparence élégante",
            font=("Segoe UI", 16, "bold"),
            bg="#1E1E1E",
            fg="white"
        )
        title.pack(anchor="w", pady=(0, 5))
        
        subtitle = tk.Label(
            container,
            text="Rendre le fond du terminal transparent tout en gardant le texte parfaitement lisible",
            font=("Segoe UI", 10),
            bg="#1E1E1E",
            fg="#888",
            wraplength=700,
            justify="left"
        )
        subtitle.pack(anchor="w", pady=(0, 25))
        
        # Card pour l'activation
        activation_card = tk.Frame(container, bg="#252526", relief=tk.FLAT)
        activation_card.pack(fill=tk.X, pady=(0, 20))
        
        activation_inner = tk.Frame(activation_card, bg="#252526")
        activation_inner.pack(fill=tk.X, padx=20, pady=20)
        
        self.transparency_enabled_var = tk.BooleanVar(value=self.terminal.window_transparency_enabled)
        
        enable_check = tk.Checkbutton(
            activation_inner,
            text="✨  Activer l'effet Glass (transparence du fond uniquement)",
            variable=self.transparency_enabled_var,
            bg="#252526",
            fg="white",
            selectcolor="#007ACC",
            font=("Segoe UI", 12, "bold"),
            command=self.on_transparency_toggle,
            activebackground="#252526",
            activeforeground="white",
            cursor="hand2"
        )
        enable_check.pack(anchor="w")
        
        # Card pour le contrôle d'opacité
        opacity_card = tk.Frame(container, bg="#252526", relief=tk.FLAT)
        opacity_card.pack(fill=tk.X, pady=(0, 20))
        
        opacity_inner = tk.Frame(opacity_card, bg="#252526")
        opacity_inner.pack(fill=tk.X, padx=20, pady=20)
        
        opacity_header = tk.Frame(opacity_inner, bg="#252526")
        opacity_header.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            opacity_header,
            text="💎  Niveau de transparence",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(side=tk.LEFT)
        
        self.window_opacity_value_label = tk.Label(
            opacity_header,
            text=f"{self.terminal.window_opacity:.2f}",
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            padx=12,
            pady=4
        )
        self.window_opacity_value_label.pack(side=tk.RIGHT)
        
        self.window_opacity_var = tk.DoubleVar(value=self.terminal.window_opacity)
        
        # Frame pour le slider
        slider_frame = tk.Frame(opacity_inner, bg="#252526")
        slider_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            slider_frame,
            text="Transparent",
            bg="#252526",
            fg="#888",
            font=("Segoe UI", 9)
        ).pack(side=tk.LEFT)
        
        tk.Label(
            slider_frame,
            text="Opaque",
            bg="#252526",
            fg="#888",
            font=("Segoe UI", 9)
        ).pack(side=tk.RIGHT)
        
        window_opacity_scale = tk.Scale(
            opacity_inner,
            from_=0.1,
            to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            variable=self.window_opacity_var,
            bg="#252526",
            fg="white",
            highlightthickness=0,
            troughcolor="#3E3E42",
            activebackground="#007ACC",
            length=700,
            command=self.on_window_opacity_change,
            showvalue=0,
            cursor="hand2"
        )
        window_opacity_scale.pack(fill=tk.X)
        
        # Préréglages rapides
        presets_card = tk.Frame(container, bg="#252526", relief=tk.FLAT)
        presets_card.pack(fill=tk.X, pady=(0, 20))
        
        presets_inner = tk.Frame(presets_card, bg="#252526")
        presets_inner.pack(fill=tk.X, padx=20, pady=20)
        
        tk.Label(
            presets_inner,
            text="⚡  Préréglages rapides",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 15))
        
        presets_buttons = tk.Frame(presets_inner, bg="#252526")
        presets_buttons.pack(fill=tk.X)
        
        presets = [
            ("💎  Subtil", 0.95, "#569CD6"),
            ("🌊  Medium", 0.85, "#4EC9B0"),
            ("🔮  Intense", 0.70, "#C586C0"),
            ("👻  Très transparent", 0.50, "#CE9178"),
            ("⚫  Opaque", 1.0, "#3E3E42")
        ]
        
        for name, opacity, color in presets:
            btn = tk.Button(
                presets_buttons,
                text=name,
                command=lambda o=opacity: self.apply_opacity_preset(o),
                bg=color,
                fg="white",
                font=("Segoe UI", 10, "bold"),
                padx=15,
                pady=8,
                relief=tk.FLAT,
                cursor="hand2",
                activebackground=color,
                activeforeground="white"
            )
            btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Informations
        info_card = tk.Frame(container, bg="#264F78", relief=tk.FLAT)
        info_card.pack(fill=tk.X)
        
        info_inner = tk.Frame(info_card, bg="#264F78")
        info_inner.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(
            info_inner,
            text="💡  Astuce",
            bg="#264F78",
            fg="#FFFFFF",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=(0, 8))
        
        info_text = """• L'effet Glass rend uniquement le fond transparent, le texte reste 100% lisible
• Fonctionne mieux avec une opacité entre 0.80 et 0.95
• Compatible Windows 10/11 pour un effet optimal
• Vous pouvez voir votre bureau et vos autres fenêtres à travers le terminal"""
        
        tk.Label(
            info_inner,
            text=info_text,
            bg="#264F78",
            fg="#D4D4D4",
            font=("Segoe UI", 10),
            justify="left",
            anchor="w"
        ).pack(fill=tk.X)
    
    def on_transparency_toggle(self):
        """Active/désactive la transparence"""
        enabled = self.transparency_enabled_var.get()
        self.terminal.window_transparency_enabled = enabled
        if enabled:
            self.terminal.apply_window_transparency()
        else:
            self.terminal.remove_window_transparency()
    
    def on_window_opacity_change(self, value):
        """Appelé quand l'opacité de la fenêtre change"""
        opacity = float(value)
        self.terminal.window_opacity = opacity
        self.window_opacity_value_label.config(text=f"{opacity:.2f}")
        if self.terminal.window_transparency_enabled:
            self.terminal.apply_window_transparency()
    
    def apply_opacity_preset(self, opacity):
        """Applique un préréglage d'opacité"""
        self.window_opacity_var.set(opacity)
        self.terminal.window_opacity = opacity
        self.window_opacity_value_label.config(text=f"{opacity:.2f}")
        self.transparency_enabled_var.set(True)
        self.terminal.window_transparency_enabled = True
        self.terminal.apply_window_transparency()
    
    def create_background_tab(self, parent):
        """Crée l'onglet de configuration de l'image de fond"""
        container = tk.Frame(parent, bg="#1E1E1E")
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        title = tk.Label(
            container,
            text="🖼️  Image de fond personnalisée",
            font=("Segoe UI", 16, "bold"),
            bg="#1E1E1E",
            fg="white"
        )
        title.pack(anchor="w", pady=(0, 5))
        
        subtitle = tk.Label(
            container,
            text="Ajoutez votre propre image pour personnaliser l'arrière-plan du terminal",
            font=("Segoe UI", 10),
            bg="#1E1E1E",
            fg="#888"
        )
        subtitle.pack(anchor="w", pady=(0, 25))
        
        # Card pour l'aperçu
        preview_card = tk.Frame(container, bg="#252526")
        preview_card.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        preview_inner = tk.Frame(preview_card, bg="#252526")
        preview_inner.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            preview_inner,
            text="Aperçu",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        self.preview_label = tk.Label(
            preview_inner,
            text="Aucune image sélectionnée",
            bg="#1E1E1E",
            fg="#888",
            font=("Segoe UI", 10),
            width=60,
            height=15
        )
        self.preview_label.pack(fill=tk.BOTH, expand=True)
        
        if self.terminal.background_image_path:
            self.update_preview(self.terminal.background_image_path)
        
        # Boutons d'action
        btn_frame = tk.Frame(container, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X, pady=(0, 20))
        
        select_btn = tk.Button(
            btn_frame,
            text="📁  Choisir une image",
            command=self.select_background_image,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        select_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        remove_btn = tk.Button(
            btn_frame,
            text="🗑️  Supprimer",
            command=self.remove_background_image,
            bg="#F48771",
            fg="white",
            font=("Segoe UI", 11),
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        remove_btn.pack(side=tk.LEFT)
        
        # Paramètres d'image
        settings_card = tk.Frame(container, bg="#252526")
        settings_card.pack(fill=tk.X)
        
        settings_inner = tk.Frame(settings_card, bg="#252526")
        settings_inner.pack(fill=tk.X, padx=20, pady=20)
        
        tk.Label(
            settings_inner,
            text="⚙️  Paramètres d'affichage",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 15))
        
        # Opacité
        opacity_frame = tk.Frame(settings_inner, bg="#252526")
        opacity_frame.pack(fill=tk.X, pady=(0, 15))
        
        opacity_label_frame = tk.Frame(opacity_frame, bg="#252526")
        opacity_label_frame.pack(fill=tk.X, pady=(0, 5))
        
        tk.Label(
            opacity_label_frame,
            text="Opacité de l'image",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side=tk.LEFT)
        
        self.opacity_label = tk.Label(
            opacity_label_frame,
            text=f"{self.terminal.background_opacity:.1f}",
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=2
        )
        self.opacity_label.pack(side=tk.RIGHT)
        
        self.opacity_var = tk.DoubleVar(value=self.terminal.background_opacity)
        opacity_scale = tk.Scale(
            opacity_frame,
            from_=0.1,
            to=1.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.opacity_var,
            bg="#252526",
            fg="white",
            highlightthickness=0,
            troughcolor="#3E3E42",
            activebackground="#007ACC",
            command=self.on_opacity_change,
            showvalue=0,
            cursor="hand2"
        )
        opacity_scale.pack(fill=tk.X)
        
        # Mode d'affichage
        stretch_frame = tk.Frame(settings_inner, bg="#252526")
        stretch_frame.pack(fill=tk.X)
        
        tk.Label(
            stretch_frame,
            text="Mode d'affichage",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        self.stretch_var = tk.StringVar(value=self.terminal.background_stretch_mode)
        
        modes_frame = tk.Frame(stretch_frame, bg="#252526")
        modes_frame.pack(fill=tk.X)
        
        stretch_modes = [
            ("Étirer", "stretch"),
            ("Ajuster", "fit"),
            ("Remplir", "fill"),
            ("Centrer", "center"),
            ("Mosaïque", "tile")
        ]
        
        for text, mode in stretch_modes:
            tk.Radiobutton(
                modes_frame,
                text=text,
                variable=self.stretch_var,
                value=mode,
                bg="#252526",
                fg="white",
                selectcolor="#007ACC",
                font=("Segoe UI", 10),
                command=self.on_stretch_change,
                activebackground="#252526",
                activeforeground="white",
                cursor="hand2"
            ).pack(side=tk.LEFT, padx=(0, 15))
    
    def select_background_image(self):
        """Sélectionne une image de fond"""
        filename = filedialog.askopenfilename(
            title="Choisir une image de fond",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpg *.jpeg"),
                ("GIF", "*.gif"),
                ("Tous les fichiers", "*.*")
            ]
        )
        
        if filename:
            self.terminal.background_image_path = filename
            self.update_preview(filename)
    
    def remove_background_image(self):
        """Supprime l'image de fond"""
        self.terminal.background_image_path = None
        self.preview_label.config(image='', text="Aucune image sélectionnée")
    
    def update_preview(self, image_path):
        """Met à jour l'aperçu de l'image"""
        try:
            img = Image.open(image_path)
            img.thumbnail((500, 300), Image.Resampling.LANCZOS)
            
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(self.opacity_var.get())
            
            photo = ImageTk.PhotoImage(img)
            self.preview_label.config(image=photo, text='')
            self.preview_label.image = photo
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger l'image:\n{e}")
    
    def on_opacity_change(self, value):
        """Appelé quand l'opacité change"""
        self.terminal.background_opacity = float(value)
        self.opacity_label.config(text=f"{float(value):.1f}")
        if self.terminal.background_image_path:
            self.update_preview(self.terminal.background_image_path)
    
    def on_stretch_change(self):
        """Appelé quand le mode d'étirement change"""
        self.terminal.background_stretch_mode = self.stretch_var.get()
    
    def create_appearance_tab(self, parent):
        """Crée l'onglet d'apparence"""
        container = tk.Frame(parent, bg="#1E1E1E")
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        title = tk.Label(
            container,
            text="🎨  Personnalisation des couleurs",
            font=("Segoe UI", 16, "bold"),
            bg="#1E1E1E",
            fg="white"
        )
        title.pack(anchor="w", pady=(0, 25))
        
        # Colors card
        colors_card = tk.Frame(container, bg="#252526")
        colors_card.pack(fill=tk.X, pady=(0, 20))
        
        colors_inner = tk.Frame(colors_card, bg="#252526")
        colors_inner.pack(fill=tk.X, padx=20, pady=20)
        
        colors = [
            ("Fond du terminal", "bg_color"),
            ("Texte principal", "fg_color"),
            ("Prompt", "prompt_color"),
            ("Succès", "success_color"),
            ("Erreur", "error_color"),
            ("Avertissement", "warning_color"),
            ("Information", "info_color"),
        ]
        
        self.color_buttons = {}
        
        for label, attr in colors:
            frame = tk.Frame(colors_inner, bg="#252526")
            frame.pack(fill=tk.X, pady=8)
            
            lbl = tk.Label(
                frame,
                text=label,
                font=("Segoe UI", 11),
                bg="#252526",
                fg="white",
                width=20,
                anchor="w"
            )
            lbl.pack(side=tk.LEFT)
            
            current_color = getattr(self.terminal, attr)
            
            btn = tk.Button(
                frame,
                text="Choisir",
                bg=current_color,
                fg="white" if self.is_dark(current_color) else "black",
                command=lambda a=attr: self.choose_color(a),
                font=("Segoe UI", 10, "bold"),
                relief=tk.FLAT,
                padx=15,
                pady=5,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=15)
            self.color_buttons[attr] = btn
            
            color_label = tk.Label(
                frame,
                text=current_color,
                font=("Segoe UI", 10),
                bg="#252526",
                fg="#888"
            )
            color_label.pack(side=tk.LEFT)
            self.color_buttons[f"{attr}_label"] = color_label
        
        # Thèmes
        themes_card = tk.Frame(container, bg="#252526")
        themes_card.pack(fill=tk.X)
        
        themes_inner = tk.Frame(themes_card, bg="#252526")
        themes_inner.pack(fill=tk.X, padx=20, pady=20)
        
        tk.Label(
            themes_inner,
            text="🎭  Thèmes prédéfinis",
            bg="#252526",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 15))
        
        theme_buttons = tk.Frame(themes_inner, bg="#252526")
        theme_buttons.pack(fill=tk.X)
        
        themes = [
            ("🌙  Sombre", self.apply_dark_theme, "#1E1E1E"),
            ("☀️  Clair", self.apply_light_theme, "#FFFFFF"),
            ("🌊  Ocean", self.apply_ocean_theme, "#0A1929"),
            ("🔥  Fire", self.apply_fire_theme, "#8B0000"),
            ("🌲  Matrix", self.apply_matrix_theme, "#00FF00"),
        ]
        
        for name, command, color in themes:
            btn = tk.Button(
                theme_buttons,
                text=name,
                command=command,
                bg="#3E3E42",
                fg="white",
                font=("Segoe UI", 10, "bold"),
                padx=15,
                pady=8,
                relief=tk.FLAT,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
    
    def create_commands_tab(self, parent):
        """Crée l'onglet des commandes personnalisées"""
        container = tk.Frame(parent, bg="#1E1E1E")
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        title = tk.Label(
            container,
            text="⚡  Commandes personnalisées",
            font=("Segoe UI", 16, "bold"),
            bg="#1E1E1E",
            fg="white"
        )
        title.pack(anchor="w", pady=(0, 5))
        
        info = tk.Label(
            container,
            text="Créez vos propres commandes pour lancer des scripts ou programmes",
            font=("Segoe UI", 10),
            bg="#1E1E1E",
            fg="#888"
        )
        info.pack(anchor="w", pady=(0, 20))
        
        # Liste
        list_card = tk.Frame(container, bg="#252526")
        list_card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        list_inner = tk.Frame(list_card, bg="#252526")
        list_inner.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        scrollbar = tk.Scrollbar(list_inner)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.commands_listbox = tk.Listbox(
            list_inner,
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 11),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.commands_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.commands_listbox.yview)
        
        self.load_custom_commands()
        
        # Boutons
        btn_frame = tk.Frame(container, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X)
        
        add_btn = tk.Button(
            btn_frame,
            text="➕  Ajouter",
            command=self.add_custom_command,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        add_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_btn = tk.Button(
            btn_frame,
            text="🗑️  Supprimer",
            command=self.delete_custom_command,
            bg="#F48771",
            fg="white",
            font=("Segoe UI", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        delete_btn.pack(side=tk.LEFT)
    
    def create_alias_tab(self, parent):
        """Crée l'onglet des alias"""
        container = tk.Frame(parent, bg="#1E1E1E")
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        title = tk.Label(
            container,
            text="🔗  Alias de commandes",
            font=("Segoe UI", 16, "bold"),
            bg="#1E1E1E",
            fg="white"
        )
        title.pack(anchor="w", pady=(0, 5))
        
        info = tk.Label(
            container,
            text="Créez des raccourcis pour vos commandes favorites",
            font=("Segoe UI", 10),
            bg="#1E1E1E",
            fg="#888"
        )
        info.pack(anchor="w", pady=(0, 20))
        
        # Liste
        list_card = tk.Frame(container, bg="#252526")
        list_card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        list_inner = tk.Frame(list_card, bg="#252526")
        list_inner.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        scrollbar = tk.Scrollbar(list_inner)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.alias_listbox = tk.Listbox(
            list_inner,
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 11),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.alias_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.alias_listbox.yview)
        
        self.load_aliases()
        
        # Boutons
        btn_frame = tk.Frame(container, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X)
        
        add_btn = tk.Button(
            btn_frame,
            text="➕  Ajouter",
            command=self.add_alias,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        add_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_btn = tk.Button(
            btn_frame,
            text="🗑️  Supprimer",
            command=self.delete_alias,
            bg="#F48771",
            fg="white",
            font=("Segoe UI", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        delete_btn.pack(side=tk.LEFT)
    
    def is_dark(self, color):
        """Vérifie si une couleur est sombre"""
        try:
            color = color.lstrip('#')
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            return brightness < 128
        except:
            return True
    
    def choose_color(self, attr):
        """Ouvre le sélecteur de couleur"""
        current_color = getattr(self.terminal, attr)
        color = colorchooser.askcolor(color=current_color, title=f"Choisir la couleur")
        
        if color[1]:
            setattr(self.terminal, attr, color[1])
            btn = self.color_buttons[attr]
            btn.config(bg=color[1], fg="white" if self.is_dark(color[1]) else "black")
            self.color_buttons[f"{attr}_label"].config(text=color[1])
    
    def apply_dark_theme(self):
        """Applique le thème sombre"""
        theme = {
            "bg_color": "#1E1E1E",
            "fg_color": "#D4D4D4",
            "prompt_color": "#4EC9B0",
            "success_color": "#4EC9B0",
            "error_color": "#F48771",
            "warning_color": "#DCDCAA",
            "info_color": "#569CD6",
        }
        self.apply_theme(theme)
    
    def apply_light_theme(self):
        """Applique le thème clair"""
        theme = {
            "bg_color": "#FFFFFF",
            "fg_color": "#000000",
            "prompt_color": "#0066CC",
            "success_color": "#008000",
            "error_color": "#CC0000",
            "warning_color": "#FF8C00",
            "info_color": "#0066CC",
        }
        self.apply_theme(theme)
    
    def apply_ocean_theme(self):
        """Applique le thème océan"""
        theme = {
            "bg_color": "#0A1929",
            "fg_color": "#B2D8E8",
            "prompt_color": "#00D9FF",
            "success_color": "#00E5A0",
            "error_color": "#FF6B9D",
            "warning_color": "#FFD700",
            "info_color": "#4DD0E1",
        }
        self.apply_theme(theme)
    
    def apply_fire_theme(self):
        """Applique le thème feu"""
        theme = {
            "bg_color": "#1A0000",
            "fg_color": "#FFE4B5",
            "prompt_color": "#FF6347",
            "success_color": "#32CD32",
            "error_color": "#FF0000",
            "warning_color": "#FFA500",
            "info_color": "#FF8C00",
        }
        self.apply_theme(theme)
    
    def apply_matrix_theme(self):
        """Applique le thème Matrix"""
        theme = {
            "bg_color": "#000000",
            "fg_color": "#00FF00",
            "prompt_color": "#00FF00",
            "success_color": "#00FF00",
            "error_color": "#FF0000",
            "warning_color": "#FFFF00",
            "info_color": "#00FF00",
        }
        self.apply_theme(theme)
    
    def apply_theme(self, theme):
        """Applique un thème"""
        for attr, color in theme.items():
            setattr(self.terminal, attr, color)
            if attr in self.color_buttons:
                btn = self.color_buttons[attr]
                btn.config(bg=color, fg="white" if self.is_dark(color) else "black")
                self.color_buttons[f"{attr}_label"].config(text=color)
    
    def load_custom_commands(self):
        """Charge les commandes personnalisées"""
        self.commands_listbox.delete(0, tk.END)
        custom_commands = self.terminal.config.get('custom_commands', {})
        for name, path in custom_commands.items():
            self.commands_listbox.insert(tk.END, f"{name} → {path}")
    
    def add_custom_command(self):
        """Ajoute une commande personnalisée"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Ajouter une commande")
        dialog.geometry("550x250")
        dialog.configure(bg="#1E1E1E")
        
        # Header
        header = tk.Frame(dialog, bg="#007ACC", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="➕  Nouvelle commande",
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=12, padx=20, anchor="w")
        
        content = tk.Frame(dialog, bg="#1E1E1E")
        content.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        tk.Label(
            content,
            text="Nom de la commande",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 5))
        
        name_entry = tk.Entry(content, font=("Segoe UI", 11), width=50, relief=tk.FLAT, bg="#252526", fg="white", insertbackground="white")
        name_entry.pack(pady=(0, 15), ipady=5)
        
        tk.Label(
            content,
            text="Chemin du script/programme",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 5))
        
        path_frame = tk.Frame(content, bg="#1E1E1E")
        path_frame.pack(fill=tk.X, pady=(0, 20))
        
        path_entry = tk.Entry(path_frame, font=("Segoe UI", 11), width=40, relief=tk.FLAT, bg="#252526", fg="white", insertbackground="white")
        path_entry.pack(side=tk.LEFT, ipady=5, fill=tk.X, expand=True, padx=(0, 10))
        
        def browse():
            filename = filedialog.askopenfilename(
                title="Sélectionner un fichier",
                filetypes=[
                    ("Tous les fichiers", "*.*"),
                    ("Scripts Python", "*.py"),
                    ("Scripts Batch", "*.bat"),
                    ("Exécutables", "*.exe")
                ]
            )
            if filename:
                path_entry.delete(0, tk.END)
                path_entry.insert(0, filename)
        
        browse_btn = tk.Button(
            path_frame,
            text="📁  Parcourir",
            command=browse,
            bg="#3E3E42",
            fg="white",
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        browse_btn.pack(side=tk.LEFT)
        
        btn_frame = tk.Frame(content, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X)
        
        def save():
            name = name_entry.get().strip()
            path = path_entry.get().strip()
            
            if not name or not path:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                return
            
            if 'custom_commands' not in self.terminal.config:
                self.terminal.config['custom_commands'] = {}
            
            self.terminal.config['custom_commands'][name] = path
            self.load_custom_commands()
            dialog.destroy()
        
        tk.Button(
            btn_frame,
            text="💾  Sauvegarder",
            command=save,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            btn_frame,
            text="❌  Annuler",
            command=dialog.destroy,
            bg="#3E3E42",
            fg="white",
            font=("Segoe UI", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT)
    
    def edit_custom_command(self):
        """Modifie une commande personnalisée"""
        selection = self.commands_listbox.curselection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une commande")
            return
        
        messagebox.showinfo("Info", "Fonctionnalité en développement")
    
    def delete_custom_command(self):
        """Supprime une commande personnalisée"""
        selection = self.commands_listbox.curselection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une commande")
            return
        
        item = self.commands_listbox.get(selection[0])
        name = item.split(" → ")[0]
        
        if messagebox.askyesno("Confirmation", f"Supprimer la commande '{name}' ?"):
            if 'custom_commands' in self.terminal.config:
                if name in self.terminal.config['custom_commands']:
                    del self.terminal.config['custom_commands'][name]
                    self.load_custom_commands()
    
    def load_aliases(self):
        """Charge les alias"""
        self.alias_listbox.delete(0, tk.END)
        for name, cmd in self.terminal.aliases.items():
            self.alias_listbox.insert(tk.END, f"{name} = {cmd}")
    
    def add_alias(self):
        """Ajoute un alias"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Ajouter un alias")
        dialog.geometry("500x220")
        dialog.configure(bg="#1E1E1E")
        
        # Header
        header = tk.Frame(dialog, bg="#007ACC", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="➕  Nouvel alias",
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=12, padx=20, anchor="w")
        
        content = tk.Frame(dialog, bg="#1E1E1E")
        content.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        tk.Label(
            content,
            text="Nom de l'alias",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 5))
        
        name_entry = tk.Entry(content, font=("Segoe UI", 11), width=50, relief=tk.FLAT, bg="#252526", fg="white", insertbackground="white")
        name_entry.pack(pady=(0, 15), ipady=5)
        
        tk.Label(
            content,
            text="Commande",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 5))
        
        cmd_entry = tk.Entry(content, font=("Segoe UI", 11), width=50, relief=tk.FLAT, bg="#252526", fg="white", insertbackground="white")
        cmd_entry.pack(pady=(0, 20), ipady=5)
        
        btn_frame = tk.Frame(content, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X)
        
        def save():
            name = name_entry.get().strip()
            cmd = cmd_entry.get().strip()
            
            if not name or not cmd:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                return
            
            self.terminal.aliases[name] = cmd
            self.load_aliases()
            dialog.destroy()
        
        tk.Button(
            btn_frame,
            text="💾  Sauvegarder",
            command=save,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            btn_frame,
            text="❌  Annuler",
            command=dialog.destroy,
            bg="#3E3E42",
            fg="white",
            font=("Segoe UI", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT)
    
    def delete_alias(self):
        """Supprime un alias"""
        selection = self.alias_listbox.curselection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner un alias")
            return
        
        item = self.alias_listbox.get(selection[0])
        name = item.split(" = ")[0]
        
        if messagebox.askyesno("Confirmation", f"Supprimer l'alias '{name}' ?"):
            if name in self.terminal.aliases:
                del self.terminal.aliases[name]
                self.load_aliases()
    
    def save_settings(self):
        """Sauvegarde les paramètres"""
        self.terminal.save_config()
        self.terminal.apply_colors()
        self.terminal.update_background()
        
        messagebox.showinfo("Succès", "✓  Paramètres sauvegardés avec succès!")
        self.window.destroy()


class TerminalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal Python - Glass Edition")
        self.root.geometry("1000x700")
        
        # Configuration
        self.current_dir = os.getcwd()
        self.history = []
        self.history_index = -1
        self.config_file = os.path.join(os.path.expanduser("~"), ".python_terminal_config.json")
        self.history_file = os.path.join(os.path.expanduser("~"), ".python_terminal_history.txt")
        
        # Charger la configuration
        self.config = self.load_config()
        self.aliases = self.config.get('aliases', {
            'll': 'dir',
            'ls': 'dir',
            'clear': 'cls',
            'cat': 'type',
        })
        
        self.last_exit_code = 0
        self.env_vars = {}
        
        # Paramètres de transparence de la fenêtre
        self.window_transparency_enabled = self.config.get('transparency', {}).get('enabled', False)
        self.window_opacity = self.config.get('transparency', {}).get('opacity', 0.95)
        
        # Paramètres de l'image de fond
        self.background_image_path = self.config.get('background', {}).get('image_path', None)
        self.background_opacity = self.config.get('background', {}).get('opacity', 0.3)
        self.background_stretch_mode = self.config.get('background', {}).get('stretch_mode', 'fill')
        self.background_label = None
        self.background_photo = None
        
        # Couleurs du thème
        saved_colors = self.config.get('colors', {})
        self.bg_color = saved_colors.get('bg_color', "#1E1E1E")
        self.fg_color = saved_colors.get('fg_color', "#D4D4D4")
        self.prompt_color = saved_colors.get('prompt_color', "#4EC9B0")
        self.success_color = saved_colors.get('success_color', "#4EC9B0")
        self.error_color = saved_colors.get('error_color', "#F48771")
        self.warning_color = saved_colors.get('warning_color', "#DCDCAA")
        self.info_color = saved_colors.get('info_color', "#569CD6")
        
        # Panneau de paramètres
        self.settings_panel = SettingsPanel(self.root, self)
        
        # Configurer l'interface
        self.setup_ui()
        self.load_history()
        
        # Appliquer la transparence si activée
        if self.window_transparency_enabled:
            self.apply_window_transparency()
        
        # Afficher le message de bienvenue
        self.print_welcome()
        self.show_prompt()
        
        # Appliquer l'image de fond si configurée
        self.update_background()
    
    def apply_window_transparency(self):
        """Applique la transparence à la fenêtre (effet glass) - FOND UNIQUEMENT"""
        try:
            self.root.update_idletasks()
            
            if platform.system() == 'Windows':
                hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
                opacity_value = int(self.window_opacity * 255)
                
                GWL_EXSTYLE = -20
                WS_EX_LAYERED = 0x00080000
                LWA_ALPHA = 0x00000002
                
                style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED)
                ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, opacity_value, LWA_ALPHA)
            else:
                self.root.attributes('-alpha', self.window_opacity)
        except Exception as e:
            print(f"Erreur lors de l'application de la transparence: {e}")
    
    def remove_window_transparency(self):
        """Retire la transparence de la fenêtre"""
        try:
            if platform.system() == 'Windows':
                hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
                GWL_EXSTYLE = -20
                WS_EX_LAYERED = 0x00080000
                
                style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style & ~WS_EX_LAYERED)
            else:
                self.root.attributes('-alpha', 1.0)
        except Exception as e:
            print(f"Erreur lors du retrait de la transparence: {e}")
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        self.root.configure(bg=self.bg_color)
        
        # Frame principale
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barre de titre moderne avec gradient
        title_frame = tk.Frame(main_frame, bg="#007ACC", height=40)
        title_frame.pack(fill=tk.X, pady=(0, 5))
        title_frame.pack_propagate(False)
        
        # Titre avec icône
        title_container = tk.Frame(title_frame, bg="#007ACC")
        title_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        title_label = tk.Label(
            title_container,
            text="💎  Terminal Python - Glass Edition",
            bg="#007ACC",
            fg="#FFFFFF",
            font=("Segoe UI", 12, "bold"),
            anchor="w",
            padx=15
        )
        title_label.pack(fill=tk.BOTH, expand=True)
        
        # Boutons modernes
        btn_frame = tk.Frame(title_frame, bg="#007ACC")
        btn_frame.pack(side=tk.RIGHT, padx=10)
        
        settings_btn = tk.Button(
            btn_frame,
            text="⚙️  Paramètres",
            command=self.settings_panel.show,
            bg="#005A9E",
            fg="#FFFFFF",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            font=("Segoe UI", 10),
            cursor="hand2",
            activebackground="#004578",
            activeforeground="white"
        )
        settings_btn.pack(side=tk.LEFT, padx=3)
        
        clear_btn = tk.Button(
            btn_frame,
            text="🗑️  Clear",
            command=self.clear_terminal,
            bg="#005A9E",
            fg="#FFFFFF",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            font=("Segoe UI", 10),
            cursor="hand2",
            activebackground="#004578",
            activeforeground="white"
        )
        clear_btn.pack(side=tk.LEFT, padx=3)
        
        # Zone de texte avec scrollbar et fond
        self.text_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label pour l'image de fond
        self.background_label = tk.Label(self.text_frame, bg=self.bg_color)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Créer la zone de texte
        self.text_area = scrolledtext.ScrolledText(
            self.text_frame,
            bg=self.bg_color,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            font=("Consolas", 11),
            wrap=tk.WORD,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.text_area.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Configurer les tags de couleur
        self.apply_colors()
        
        # Barre de statut moderne
        status_frame = tk.Frame(main_frame, bg="#007ACC", height=30)
        status_frame.pack(fill=tk.X, pady=(5, 0))
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"📁  {self.current_dir}",
            bg="#007ACC",
            fg="#FFFFFF",
            font=("Segoe UI", 10),
            anchor="w",
            padx=15
        )
        self.status_label.pack(fill=tk.BOTH)
        
        # Bindings
        self.text_area.bind("<Return>", self.on_enter)
        self.text_area.bind("<Up>", self.on_up_arrow)
        self.text_area.bind("<Down>", self.on_down_arrow)
        self.text_area.bind("<Tab>", self.on_tab)
        self.text_area.bind("<Control-c>", self.on_ctrl_c)
        self.text_area.bind("<Control-l>", lambda e: self.clear_terminal())
        self.text_area.bind("<Key>", self.on_key_press)
        self.text_area.bind("<BackSpace>", self.on_backspace)
        self.text_area.bind("<Configure>", self.on_resize)
        
        # Marquer la fin du prompt
        self.text_area.mark_set("prompt_end", "1.0")
        self.text_area.mark_gravity("prompt_end", tk.LEFT)
    
    def on_resize(self, event):
        """Appelé quand la fenêtre est redimensionnée"""
        if self.background_image_path:
            self.root.after(100, self.update_background)
    
    def update_background(self):
        """Met à jour l'image de fond"""
        if not self.background_image_path or not os.path.exists(self.background_image_path):
            self.background_label.config(image='')
            return
        
        try:
            img = Image.open(self.background_image_path)
            
            width = self.text_frame.winfo_width()
            height = self.text_frame.winfo_height()
            
            if width <= 1 or height <= 1:
                width = 1000
                height = 600
            
            if self.background_stretch_mode == 'stretch':
                img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            elif self.background_stretch_mode == 'fit':
                img.thumbnail((width, height), Image.Resampling.LANCZOS)
                new_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                x = (width - img.width) // 2
                y = (height - img.height) // 2
                new_img.paste(img, (x, y))
                img = new_img
            
            elif self.background_stretch_mode == 'fill':
                img_ratio = img.width / img.height
                target_ratio = width / height
                
                if img_ratio > target_ratio:
                    new_height = height
                    new_width = int(height * img_ratio)
                else:
                    new_width = width
                    new_height = int(width / img_ratio)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                left = (new_width - width) // 2
                top = (new_height - height) // 2
                img = img.crop((left, top, left + width, top + height))
            
            elif self.background_stretch_mode == 'center':
                new_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                x = (width - img.width) // 2
                y = (height - img.height) // 2
                new_img.paste(img, (x, y))
                img = new_img
            
            elif self.background_stretch_mode == 'tile':
                new_img = Image.new('RGBA', (width, height))
                for y in range(0, height, img.height):
                    for x in range(0, width, img.width):
                        new_img.paste(img, (x, y))
                img = new_img
            
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            alpha = img.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(self.background_opacity)
            img.putalpha(alpha)
            
            self.background_photo = ImageTk.PhotoImage(img)
            self.background_label.config(image=self.background_photo)
            
        except Exception as e:
            print(f"Erreur lors du chargement de l'image de fond: {e}")
            self.background_label.config(image='')
    
    def apply_colors(self):
        """Applique les couleurs au terminal"""
        self.text_area.config(bg=self.bg_color, fg=self.fg_color, insertbackground=self.fg_color)
        self.root.configure(bg=self.bg_color)
        
        self.text_area.tag_config("prompt", foreground=self.prompt_color, font=("Consolas", 11, "bold"))
        self.text_area.tag_config("success", foreground=self.success_color)
        self.text_area.tag_config("error", foreground=self.error_color)
        self.text_area.tag_config("warning", foreground=self.warning_color)
        self.text_area.tag_config("info", foreground=self.info_color)
        self.text_area.tag_config("command", foreground="#CE9178")
    
    def on_key_press(self, event):
        """Empêche la modification du texte avant le prompt"""
        if event.keysym in ['Up', 'Down', 'Left', 'Right', 'Control_L', 'Control_R', 
                            'Shift_L', 'Shift_R', 'Alt_L', 'Alt_R']:
            return
        
        current_pos = self.text_area.index("insert")
        prompt_pos = self.text_area.index("prompt_end")
        
        if self.text_area.compare(current_pos, "<", prompt_pos):
            return "break"
    
    def on_backspace(self, event):
        """Empêche la suppression du prompt"""
        current_pos = self.text_area.index("insert")
        prompt_pos = self.text_area.index("prompt_end")
        
        if self.text_area.compare(current_pos, "<=", prompt_pos):
            return "break"
    
    def load_config(self):
        """Charge la configuration"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def save_config(self):
        """Sauvegarde la configuration"""
        try:
            self.config['colors'] = {
                'bg_color': self.bg_color,
                'fg_color': self.fg_color,
                'prompt_color': self.prompt_color,
                'success_color': self.success_color,
                'error_color': self.error_color,
                'warning_color': self.warning_color,
                'info_color': self.info_color,
            }
            self.config['aliases'] = self.aliases
            
            self.config['background'] = {
                'image_path': self.background_image_path,
                'opacity': self.background_opacity,
                'stretch_mode': self.background_stretch_mode,
            }
            
            self.config['transparency'] = {
                'enabled': self.window_transparency_enabled,
                'opacity': self.window_opacity,
            }
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
    
    def load_history(self):
        """Charge l'historique"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.history = [line.strip() for line in f.readlines()]
        except:
            pass
    
    def save_history(self):
        """Sauvegarde l'historique"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                for cmd in self.history[-1000:]:
                    f.write(cmd + '\n')
        except:
            pass
    
    def print_welcome(self):
        """Affiche le message de bienvenue"""
        welcome = f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║          Terminal Python pour Windows - GUI                ║
║                                                            ║
║                   Version 8.0 FINALE                       ║
║         💎 Glass Edition - Design Moderne 💎              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

Commandes utiles:
  • %SETTINGS%      - Ouvrir le panneau de paramètres moderne
  • help            - Aide complète
  • clear/cls       - Effacer l'écran
  • exit/quit       - Quitter le terminal

Raccourcis:
  • Ctrl+L          - Effacer l'écran
  • Ctrl+C          - Annuler
  • ↑/↓             - Naviguer dans l'historique

Fonctionnalités:
  • 💎 Effet Glass transparent (fond uniquement!)
  • 🖼️ Image de fond personnalisable
  • 🎨 Design moderne style Windows 11
  • ⚡ Interface fluide et élégante

{'─'*60}

"""
        self.print_text(welcome, "info")
    
    def show_prompt(self):
        """Affiche le prompt"""
        username = os.environ.get('USERNAME', 'user')
        hostname = os.environ.get('COMPUTERNAME', 'PC')
        
        current_path = self.current_dir
        if len(current_path) > 40:
            parts = Path(current_path).parts
            if len(parts) > 3:
                current_path = os.path.join(parts[0], '...', *parts[-2:])
        
        status = "✓" if self.last_exit_code == 0 else "✗"
        prompt = f"\n{status} {username}@{hostname}:{current_path}$ "
        
        self.text_area.insert(tk.END, prompt, "prompt")
        self.text_area.mark_set("prompt_end", "insert")
        self.text_area.see(tk.END)
        
        self.status_label.config(text=f"📁  {self.current_dir}")
    
    def print_text(self, text, tag=""):
        """Affiche du texte avec un tag optionnel"""
        self.text_area.insert(tk.END, text, tag)
        self.text_area.see(tk.END)
    
    def print_success(self, text):
        """Affiche un message de succès"""
        self.print_text(f"✓ {text}\n", "success")
    
    def print_error(self, text):
        """Affiche un message d'erreur"""
        self.print_text(f"✗ Erreur: {text}\n", "error")
    
    def print_warning(self, text):
        """Affiche un avertissement"""
        self.print_text(f"⚠ {text}\n", "warning")
    
    def print_info(self, text):
        """Affiche une information"""
        self.print_text(f"ℹ {text}\n", "info")
    
    def get_current_command(self):
        """Récupère la commande actuelle"""
        return self.text_area.get("prompt_end", "insert")
    
    def clear_current_command(self):
        """Efface la commande actuelle"""
        self.text_area.delete("prompt_end", tk.END)
    
    def on_enter(self, event):
        """Gère l'appui sur Entrée"""
        command = self.get_current_command().strip()
        
        self.text_area.insert(tk.END, "\n")
        
        if command:
            self.history.append(command)
            self.history_index = len(self.history)
            self.execute_command(command)
        else:
            self.show_prompt()
        
        return "break"
    
    def on_up_arrow(self, event):
        """Navigation dans l'historique (haut)"""
        if self.history and self.history_index > 0:
            self.history_index -= 1
            self.clear_current_command()
            self.text_area.insert(tk.END, self.history[self.history_index])
        return "break"
    
    def on_down_arrow(self, event):
        """Navigation dans l'historique (bas)"""
        if self.history and self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.clear_current_command()
            self.text_area.insert(tk.END, self.history[self.history_index])
        elif self.history_index == len(self.history) - 1:
            self.history_index = len(self.history)
            self.clear_current_command()
        return "break"
    
    def on_tab(self, event):
        """Autocomplétion"""
        return "break"
    
    def on_ctrl_c(self, event):
        """Annulation avec Ctrl+C"""
        self.print_warning("Commande annulée")
        self.show_prompt()
        return "break"
    
    def clear_terminal(self):
        """Efface le terminal"""
        self.text_area.delete(1.0, tk.END)
        self.show_prompt()
    
    def execute_command(self, cmd_line):
        """Exécute une commande"""
        if cmd_line.upper() == "%SETTINGS%":
            self.settings_panel.show()
            self.show_prompt()
            return
        
        if cmd_line.startswith('%') and cmd_line.endswith('%'):
            var_name = cmd_line[1:-1]
            value = os.environ.get(var_name, '')
            if value:
                self.print_text(f"{var_name}={value}\n", "success")
            else:
                self.print_warning(f"Variable '{var_name}' non définie")
            self.show_prompt()
            return
        
        parts = cmd_line.split()
        if parts and parts[0] in self.aliases:
            parts[0] = self.aliases[parts[0]]
            cmd_line = ' '.join(parts)
        
        if not parts:
            self.show_prompt()
            return
        
        command = parts[0]
        args = parts[1:]
        
        custom_commands = self.config.get('custom_commands', {})
        if command in custom_commands:
            script_path = custom_commands[command]
            self.run_custom_script(script_path, args)
            self.show_prompt()
            return
        
        builtin_result = self.execute_builtin(command, args)
        if builtin_result is not None:
            self.show_prompt()
            return
        
        self.execute_system(cmd_line)
        self.show_prompt()
    
    def run_custom_script(self, script_path, args):
        """Exécute un script personnalisé"""
        def run():
            try:
                cmd = [script_path] + args
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=self.current_dir
                )
                
                stdout, stderr = process.communicate()
                self.root.after(0, lambda: self.display_output(stdout, stderr, process.returncode))
                
            except Exception as e:
                self.root.after(0, lambda: self.print_error(str(e)))
        
        thread = threading.Thread(target=run, daemon=True)
        thread.start()
    
    def execute_builtin(self, command, args):
        """Exécute les commandes intégrées"""
        builtins = {
            'cd': self.cmd_cd,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'pwd': self.cmd_pwd,
            'echo': self.cmd_echo,
            'clear': self.cmd_clear,
            'cls': self.cmd_clear,
            'help': self.cmd_help,
            'alias': self.cmd_alias,
            'set': self.cmd_set,
            'env': self.cmd_env,
            'history': self.cmd_history,
            'date': self.cmd_date,
            'time': self.cmd_time,
            'calc': self.cmd_calc,
            'sysinfo': self.cmd_sysinfo,
        }
        
        if command in builtins:
            return builtins[command](args)
        return None
    
    def cmd_cd(self, args):
        """Change de répertoire"""
        try:
            if not args:
                new_dir = os.path.expanduser("~")
            elif args[0] == '-':
                new_dir = os.environ.get('OLDPWD', os.path.expanduser("~"))
            else:
                new_dir = args[0]
            
            if not os.path.isabs(new_dir):
                new_dir = os.path.join(self.current_dir, new_dir)
            
            new_dir = os.path.normpath(new_dir)
            
            if os.path.isdir(new_dir):
                os.environ['OLDPWD'] = self.current_dir
                os.chdir(new_dir)
                self.current_dir = os.getcwd()
                self.last_exit_code = 0
            else:
                self.print_error(f"Le répertoire '{new_dir}' n'existe pas")
                self.last_exit_code = 1
        except Exception as e:
            self.print_error(f"Changement de répertoire: {e}")
            self.last_exit_code = 1
        return True
    
    def cmd_exit(self, args):
        """Quitte le terminal"""
        self.save_history()
        self.save_config()
        self.root.quit()
        return True
    
    def cmd_pwd(self, args):
        """Affiche le répertoire courant"""
        self.print_text(f"{self.current_dir}\n", "info")
        return True
    
    def cmd_echo(self, args):
        """Affiche du texte"""
        self.print_text(' '.join(args) + "\n")
        return True
    
    def cmd_clear(self, args):
        """Efface l'écran"""
        self.clear_terminal()
        return True
    
    def cmd_help(self, args):
        """Affiche l'aide"""
        help_text = """
╔════════════════════════════════════════════════════════════╗
║                    AIDE - Commandes                        ║
╚════════════════════════════════════════════════════════════╝

Spéciales:
  %SETTINGS%      Ouvrir le panneau de paramètres

Navigation:
  cd [dir]        Change de répertoire
  pwd             Affiche le répertoire courant
  dir/ls          Liste les fichiers

Système:
  echo [texte]    Affiche du texte
  clear/cls       Efface l'écran
  set [var]       Affiche une variable
  env             Toutes les variables
  sysinfo         Infos système

Utilitaires:
  calc [expr]     Calculatrice
  date            Date actuelle
  time            Heure actuelle
  history         Historique des commandes

Configuration:
  alias           Voir/créer des alias
  help            Cette aide
  exit/quit       Quitter

Personnalisation:
  • 💎 Effet Glass: Fond transparent uniquement
  • 🖼️ Image de fond personnalisable
  • 🎨 Thèmes de couleurs modernes
  • ⚡ Design Windows 11

Tapez %SETTINGS% pour découvrir toutes les options!

"""
        self.print_text(help_text, "info")
        return True
    
    def cmd_alias(self, args):
        """Gère les alias"""
        if not args:
            if not self.aliases:
                self.print_info("Aucun alias défini. Utilisez %SETTINGS% pour en créer.")
            else:
                self.print_text("\nAlias définis:\n", "info")
                for name, cmd in sorted(self.aliases.items()):
                    self.print_text(f"  {name:15s} → {cmd}\n", "success")
        return True
    
    def cmd_set(self, args):
        """Affiche les variables d'environnement"""
        if not args:
            for key, value in sorted(os.environ.items()):
                self.print_text(f"{key}={value}\n", "success")
        else:
            for arg in args:
                value = os.environ.get(arg, '')
                if value:
                    self.print_text(f"{arg}={value}\n", "success")
                else:
                    self.print_warning(f"Variable '{arg}' non définie")
        return True
    
    def cmd_env(self, args):
        """Affiche toutes les variables"""
        for key, value in sorted(os.environ.items()):
            self.print_text(f"{key}={value}\n", "info")
        return True
    
    def cmd_history(self, args):
        """Affiche l'historique"""
        if args and args[0] == '-c':
            self.history = []
            self.print_success("Historique effacé")
        else:
            for i, cmd in enumerate(self.history, 1):
                self.print_text(f"{i:4d}  {cmd}\n")
        return True
    
    def cmd_date(self, args):
        """Affiche la date"""
        now = datetime.now()
        self.print_text(f"{now.strftime('%A %d %B %Y')}\n", "info")
        return True
    
    def cmd_time(self, args):
        """Affiche l'heure"""
        now = datetime.now()
        self.print_text(f"{now.strftime('%H:%M:%S')}\n", "info")
        return True
    
    def cmd_calc(self, args):
        """Calculatrice"""
        if not args:
            self.print_error("Usage: calc [expression]")
            return True
        
        expr = ' '.join(args)
        try:
            result = eval(expr, {"__builtins__": {}}, {})
            self.print_text(f"{expr} = ", "info")
            self.print_text(f"{result}\n", "success")
        except Exception as e:
            self.print_error(f"Expression invalide: {e}")
        return True
    
    def cmd_sysinfo(self, args):
        """Informations système"""
        info = f"""
Système:         {platform.system()}
Version:         {platform.version()}
Architecture:    {platform.machine()}
Processeur:      {platform.processor()}
Python:          {platform.python_version()}
Utilisateur:     {os.environ.get('USERNAME', 'N/A')}
Machine:         {os.environ.get('COMPUTERNAME', 'N/A')}
Répertoire:      {self.current_dir}
"""
        self.print_text(info, "info")
        return True
    
    def execute_system(self, cmd_line):
        """Exécute une commande système"""
        def run_command():
            try:
                process = subprocess.Popen(
                    cmd_line,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=self.current_dir
                )
                
                stdout, stderr = process.communicate()
                self.root.after(0, lambda: self.display_output(stdout, stderr, process.returncode))
                
            except Exception as e:
                self.root.after(0, lambda: self.print_error(str(e)))
        
        thread = threading.Thread(target=run_command, daemon=True)
        thread.start()
    
    def display_output(self, stdout, stderr, returncode):
        """Affiche la sortie d'une commande"""
        if stdout:
            self.print_text(stdout)
        if stderr:
            self.print_text(stderr, "error")
        
        self.last_exit_code = returncode


def main():
    """Point d'entrée principal"""
    root = tk.Tk()
    app = TerminalGUI(root)
    
    def on_closing():
        app.save_history()
        app.save_config()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()