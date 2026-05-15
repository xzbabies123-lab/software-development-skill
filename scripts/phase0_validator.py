#!/usr/bin/env python3
"""
Phase 0验证脚本 - 强制验证苏格拉底提问是否符合规范
"""

import sys
import re

def extract_questions(text):
    """提取问题"""
    # 匹配以?结尾的句子
    questions = re.findall(r'[^。！？\n]*[？?]', text)
    return questions

def extract_options(text):
    """提取选项"""
    # 匹配A. B. C. D.格式
    options = re.findall(r'[A-D][\.、]', text)
    return options

def extract_suggestions(text):
    """提取建议"""
    # 匹配"建议"、"推荐"等关键词
    suggestions = re.findall(r'建议[：:][^\n]+|推荐[：:][^\n]+', text)
    return suggestions

def validate_phase0_output(output_text):
    """验证Phase 0输出是否符合规范"""
    
    errors = []
    
    # 检查1：是否只问了1个问题
    questions = extract_questions(output_text)
    if len(questions) > 1:
        errors.append(f"❌ 违规：问了{len(questions)}个问题，必须只问1个")
    
    # 检查2：是否提供了至少3个选项
    options = extract_options(output_text)
    if len(options) < 3:
        errors.append(f"❌ 违规：只提供了{len(options)}个选项，至少3个")
    
    # 检查3：是否有建议
    suggestions = extract_suggestions(output_text)
    if len(suggestions) == 0:
        errors.append("❌ 违规：未提供建议")
    
    # 检查4：是否生成了需求文档
    if "需求" not in output_text and "功能" not in output_text:
        errors.append("❌ 违规：未生成需求文档")
    
    if errors:
        return {"valid": False, "errors": errors}
    else:
        return {"valid": True}

if __name__ == "__main__":
    # 从stdin读取输出文本
    print("【Phase 0验证】")
    print("请输入Phase 0的输出文本（输入完成后按Ctrl+D）：")
    
    output_text = sys.stdin.read()
    
    result = validate_phase0_output(output_text)
    
    if result["valid"]:
        print("\n✅ Phase 0验证通过")
        sys.exit(0)
    else:
        print("\n❌ Phase 0验证失败：")
        for error in result["errors"]:
            print(f"   {error}")
        print("\n请重新执行Phase 0。")
        sys.exit(1)