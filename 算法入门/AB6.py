class Solution:
    def solve(self , s ):
        s = s.strip()
        stack = []
        res = 0
        num = 0
        sign = '+' 
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            # 遇到左括号
            if s[index] == '(': 
                end = index + 1
                lens = 1
                while lens > 0: 
                    if s[end] == '(':
                        lens += 1
                    if s[end] == ')':
                        lens -= 1
                    end += 1
                #将括号视为子问题进入递归
                num = self.solve(s[index + 1: end - 1]) 
                index = end - 1
                continue
            #字符数字转换成int数字
            if '0' <= s[index] <= '9':
                num = num * 10 + int(s[index])
            #根据符号运算
            if not '0' <= s[index] <= '9' or index == len(s) - 1:
                #加
                if sign == '+': 
                    stack.append(num)
                #减，加相反数
                elif sign == '-': 
                    stack.append(-1 * num)
                #乘优先计算
                elif sign == '*': 
                    stack.append(stack.pop() * num) 
                num = 0
                sign = s[index]
            index += 1
        #栈中元素相加
        while stack: 
            res += stack.pop()
        return res
