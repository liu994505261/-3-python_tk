#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
今日运势应用
适用于树莓派32位系统
"""

import tkinter as tk
from tkinter import font
import random
from datetime import datetime


class FortuneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("今日运势")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # 设置背景色
        self.root.configure(bg="#f0f0f0")
        
        # 运势类型和对应的颜色
        self.fortune_types = {
            "大吉": "#ff6b6b",
            "中吉": "#ff8787",
            "小吉": "#ffa07a",
            "吉": "#ffb347",
            "半吉": "#ffd700",
            "末吉": "#98d8c8",
            "末小吉": "#87ceeb",
            "凶": "#9370db",
            "小凶": "#b19cd9",
            "半凶": "#c8a2c8"
        }
        
        # 运势建议
        self.fortune_advice = [
            "今天适合尝试新事物",
            "保持积极心态，好运自然来",
            "多与朋友交流，会有意外收获",
            "注意休息，身体是革命的本钱",
            "今天适合学习新知识",
            "保持耐心，好事即将发生",
            "多做善事，福报自来",
            "今天适合整理思绪，规划未来",
            "保持微笑，世界会对你温柔以待",
            "相信自己，你比想象中更强大"
        ]
        
        # 幸运数字、颜色、方位
        self.lucky_numbers = list(range(1, 100))
        self.lucky_colors = ["红色", "蓝色", "绿色", "黄色", "紫色", "橙色", "粉色", "白色"]
        self.lucky_directions = ["东", "南", "西", "北", "东南", "西南", "东北", "西北"]
        
        self.setup_ui()
        
    def setup_ui(self):
        # 标题
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(
            self.root,
            text="🌟 今日运势 🌟",
            font=title_font,
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # 日期显示
        date_str = datetime.now().strftime("%Y年%m月%d日")
        date_label = tk.Label(
            self.root,
            text=date_str,
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        date_label.pack(pady=5)
        
        # 运势结果框
        self.result_frame = tk.Frame(self.root, bg="#fff", relief=tk.RAISED, borderwidth=2)
        self.result_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        # 运势等级
        self.fortune_label = tk.Label(
            self.result_frame,
            text="点击按钮查看运势",
            font=("Arial", 28, "bold"),
            bg="#fff",
            fg="#999"
        )
        self.fortune_label.pack(pady=20)
        
        # 运势建议
        self.advice_label = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 11),
            bg="#fff",
            fg="#555",
            wraplength=300,
            justify=tk.CENTER
        )
        self.advice_label.pack(pady=10)
        
        # 幸运信息
        self.lucky_label = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 10),
            bg="#fff",
            fg="#666",
            justify=tk.LEFT
        )
        self.lucky_label.pack(pady=10)
        
        # 抽取运势按钮
        button_font = font.Font(family="Arial", size=14, weight="bold")
        self.draw_button = tk.Button(
            self.root,
            text="抽取今日运势",
            font=button_font,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            cursor="hand2",
            relief=tk.RAISED,
            borderwidth=3,
            command=self.draw_fortune
        )
        self.draw_button.pack(pady=20, ipadx=20, ipady=10)
        
    def draw_fortune(self):
        # 随机选择运势
        fortune_type = random.choice(list(self.fortune_types.keys()))
        fortune_color = self.fortune_types[fortune_type]
        
        # 随机选择建议
        advice = random.choice(self.fortune_advice)
        
        # 随机生成幸运信息
        lucky_number = random.choice(self.lucky_numbers)
        lucky_color = random.choice(self.lucky_colors)
        lucky_direction = random.choice(self.lucky_directions)
        
        # 更新显示
        self.fortune_label.config(text=fortune_type, fg=fortune_color)
        self.advice_label.config(text=f"💡 {advice}")
        
        lucky_info = f"🍀 幸运数字: {lucky_number}\n🎨 幸运颜色: {lucky_color}\n🧭 幸运方位: {lucky_direction}"
        self.lucky_label.config(text=lucky_info)


def main():
    root = tk.Tk()
    app = FortuneApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
