#!/usr/bin/env python3
"""
每日测验生成器
用于自动生成每日的测验题目
"""

import json
import random
from datetime import datetime
from pathlib import Path

class QuizGenerator:
    def __init__(self):
        self.templates_dir = Path(__file__).parent
        self.quizzes_dir = Path("../daily-quizzes")

    def generate_quiz(self, day, topic):
        """生成每日测验"""
        quiz_content = f"""# Day {day} 测验 - {topic}

## 📝 知识回顾
本日重点：{topic}

---

## ✅ 选择题（每题5分，共25分）

### 1. 下列关于Go语言的描述，正确的是？
A. Go是编译型语言
B. Go支持继承
C. Go是动态类型语言
D. Go不需要编译器

**正确答案：** A
**解析：** Go是静态编译型语言，不支持继承，通过组合实现。

### 2. goroutine的调度模型是？
A. 协程调度
B. 线程调度
C. GMP模型
D. 事件循环

**正确答案：** C
**解析：** Go使用G-M-P调度模型，G代表goroutine，M代表machine(线程)，P代表processor。

### 3. CAP定理中的C、A、P分别代表？
A. 一致性、可用性、分区容错性
B. 可靠性、可用性、分区容错性
C. 一致性、准确性、分区容错性
D. 一致性、可用性、持久性

**正确答案：** A
**解析：** CAP定理：分布式系统无法同时满足一致性、可用性、分区容错性。

---

## 🖥️ 编程题（每题25分，共50分）

### 题目1：反转字符串
**要求：** 使用Go语言编写一个函数，就地反转字符串中的字节序列。

**示例：**
输入："hello"
输出："olleh"

**代码模板：**
```go
package main

import "fmt"

func reverseString(s []byte) {
    // TODO: 实现反转逻辑
}

func main() {
    s := []byte("hello")
    reverseString(s)
    fmt.Println(string(s)) // 应输出: olleh
}
```

**评分标准：**
- 正确实现双指针交换（15分）
- 边界情况处理（5分）
- 代码规范（5分）

---

### 题目2：实现LRU缓存
**要求：** 设计并实现一个LRU缓存，支持get和put操作，时间复杂度O(1)。

**接口定义：**
```go
type LRUCache struct {
    // TODO: 实现LRU缓存结构
}

func Constructor(capacity int) LRUCache

func (this *LRUCache) Get(key int) int

func (this *LRUCache) Put(key int, value int)
```

**评分标准：**
- 使用双向链表+哈希表实现（15分）
- 正确实现get/put逻辑（8分）
- 边界情况处理（2分）

---

## 📖 问答题（每题25分，共50分）

### 问题1：解释TCP四次挥手的过程
**要求：** 详细描述TCP连接关闭的流程，包括各个状态转换。

**参考答案要点：**
1. 主动方发送FIN，进入FIN_WAIT_1状态
2. 被动方回应ACK，进入CLOSE_WAIT状态
3. 被动方发送FIN，进入LAST_ACK状态
4. 主动方回应ACK，进入TIME_WAIT状态

---

### 问题2：Redis的持久化机制对比
**要求：** 比较RDB和AOF两种持久化方式的优缺点和适用场景。

**参考答案要点：**
1. RDB：快照方式，文件小，恢复快，但可能丢数据
2. AOF：日志方式，数据安全，恢复慢，文件大
3. 混合持久化：结合两者优点

---

## 📊 答案提交

请将答案提交到 ../progress/day{day}-answers.md 文件中

提交格式：
```markdown
# Day {day} 答案

## 选择题
1. A
2. C
3. A

## 编程题
### 题目1代码
```go

```

### 题目2代码
```go

```

## 问答题
### 问题1答案

### 问题2答案

```

---

## 🔍 自我评估
完成测验后，请按以下标准自我评分：
- 120分以上：🌟 优秀
- 90-119分：✅ 良好
- 60-89分：⚠️ 需要加强
- 60分以下：📚 重新学习

---
*测验生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        # 创建测验文件
        quiz_file = self.quizzes_dir / f"day{day}-quiz.md"
        quiz_file.parent.mkdir(exist_ok=True)

        with open(quiz_file, 'w', encoding='utf-8') as f:
            f.write(quiz_content)

        print(f"✅ 已生成 Day {day} 测验: {quiz_file}")

if __name__ == "__main__":
    generator = QuizGenerator()

    # 示例：生成第1天的测验
    generator.generate_quiz(1, "Go语言基础语法")