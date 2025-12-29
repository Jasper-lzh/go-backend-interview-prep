#!/usr/bin/env python3
"""
Go后端开发工程师学习计划快速启动脚本
"""

import os
import sys
from datetime import datetime
from pathlib import Path

def main():
    print("🚀 Go后端开发工程师6周学习计划")
    print("=" * 50)

    # 获取用户信息
    name = input("请输入你的姓名: ")
    start_date = input("请输入开始日期(YYYY-MM-DD)，默认今天: ")

    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")

    print(f"\n✨ 欢迎你, {name}!")
    print(f"📅 开始日期: {start_date}")
    print(f"🎯 目标: 6周内完成所有学习计划")

    # 创建个人进度文件
    progress_file = Path("progress") / f"{name}-tracker.md"
    if not progress_file.exists():
        with open(progress_file, 'w', encoding='utf-8') as f:
            f.write(f"""# {name} 的学习进度

## 📊 基本信息
- **姓名**: {name}
- **开始日期**: {start_date}
- **目标岗位**: Go后端开发工程师

## 🎯 今日任务
- [ ] 阅读Week 1学习计划
- [ ] 完成Day 1的学习内容
- [ ] 提交今日学习笔记
- [ ] 完成每日测验

## 📈 学习进度
### Week 1 [0/100%]
- [ ] Day 1: Go语法基础
- [ ] Day 2: Slice和Map深入
- [ ] ...

## 💪 学习日志
### {start_date}
- 学习时长:
- 完成内容:
- 遇到问题:
- 明日计划:
""")
        print(f"✅ 已创建你的专属进度文件: {progress_file}")

    # 提示下一步
    print("\n📌 下一步操作:")
    print("1. cd weeks/week1 # 查看第1周计划")
    print("2. cp ../templates/daily-note.md ../progress/day-1.md")
    print("3. 开始你的学习之旅!")

    print("\n💡 每日执行:")
    print("python3 start.py # 查看进度")
    print("python3 templates/quiz-generator.py # 生成新测验")

if __name__ == "__main__":
    main()