#!/usr/bin/env python3
"""
Phase 4验证脚本 - 验证测试报告和截图证据
"""

import sys
import os
import json

def validate_phase4_output(test_report_path="/tmp/test_report.json", screenshot_dir="/tmp"):
    """验证Phase 4输出是否符合规范"""
    
    errors = []
    
    # 检查1：是否有测试报告
    if not os.path.exists(test_report_path):
        errors.append("❌ 违规：未生成测试报告")
        return {"valid": False, "errors": errors}
    
    # 读取测试报告
    try:
        with open(test_report_path, 'r') as f:
            test_report = json.load(f)
    except:
        errors.append("❌ 违规：测试报告格式错误")
        return {"valid": False, "errors": errors}
    
    # 检查2：每个验收标准是否有截图
    acceptance_criteria = test_report.get("acceptance_criteria", [])
    for criteria in acceptance_criteria:
        if not criteria.get("screenshot"):
            errors.append(f"❌ 违规：验收标准'{criteria.get('name', '未知')}'缺少截图证据")
    
    # 检查3：是否所有验收标准都通过
    failed_criteria = [c for c in acceptance_criteria if c.get("status") != "PASS"]
    if failed_criteria:
        errors.append(f"❌ 违规：{len(failed_criteria)}个验收标准未通过")
    
    # 检查4：Dev↔QA Loop次数
    retry_count = test_report.get("retry_count", 0)
    if retry_count > 3:
        errors.append(f"❌ 违规：重试次数{retry_count}次，超过限制（最多3次）")
    
    # 检查5：截图文件是否存在
    for criteria in acceptance_criteria:
        screenshot = criteria.get("screenshot")
        if screenshot and not os.path.exists(screenshot):
            errors.append(f"❌ 违规：截图文件不存在：{screenshot}")
    
    if errors:
        return {"valid": False, "errors": errors}
    else:
        return {
            "valid": True,
            "total_criteria": len(acceptance_criteria),
            "passed_criteria": len([c for c in acceptance_criteria if c.get("status") == "PASS"]),
            "retry_count": retry_count
        }

if __name__ == "__main__":
    print("【Phase 4验证】")
    
    result = validate_phase4_output()
    
    if result["valid"]:
        print("\n✅ Phase 4验证通过")
        print(f"   验收标准：{result['passed_criteria']}/{result['total_criteria']}通过")
        print(f"   重试次数：{result['retry_count']}/3")
        sys.exit(0)
    else:
        print("\n❌ Phase 4验证失败：")
        for error in result["errors"]:
            print(f"   {error}")
        print("\n请重新执行Phase 4。")
        sys.exit(1)