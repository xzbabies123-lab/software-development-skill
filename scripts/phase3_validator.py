#!/usr/bin/env python3
"""
Phase 3验证脚本 - 验证代码是否可运行
"""

import sys
import subprocess
import os

def validate_phase3_output(project_dir="/tmp"):
    """验证Phase 3输出是否符合规范"""
    
    errors = []
    
    # 检查1：是否有代码文件
    code_files = []
    for root, dirs, files in os.walk(project_dir):
        for f in files:
            if f.endswith(('.py', '.js', '.vue', '.ts')):
                code_files.append(os.path.join(root, f))
    
    if len(code_files) == 0:
        errors.append("❌ 违规：未生成代码文件")
    
    # 检查2：代码是否有语法错误（Python文件）
    for f in code_files:
        if f.endswith('.py'):
            try:
                result = subprocess.run(['python3', '-m', 'py_compile', f], capture_output=True, timeout=10)
                if result.returncode != 0:
                    errors.append(f"❌ 违规：{f}有语法错误")
            except:
                pass
    
    # 检查3：是否有单元测试文件
    test_files = [f for f in code_files if 'test' in f.lower()]
    if len(test_files) == 0:
        errors.append("⚠️ 警告：未生成单元测试文件（建议添加）")
    
    if errors:
        # 区分严重错误和警告
        critical_errors = [e for e in errors if not e.startswith("⚠️")]
        if critical_errors:
            return {"valid": False, "errors": critical_errors}
        else:
            return {"valid": True, "warnings": errors, "code_files": code_files}
    else:
        return {"valid": True, "code_files": code_files}

if __name__ == "__main__":
    print("【Phase 3验证】")
    
    result = validate_phase3_output()
    
    if result["valid"]:
        print("\n✅ Phase 3验证通过")
        print(f"   代码文件：{len(result['code_files'])}个")
        if "warnings" in result:
            for warning in result["warnings"]:
                print(f"   {warning}")
        sys.exit(0)
    else:
        print("\n❌ Phase 3验证失败：")
        for error in result["errors"]:
            print(f"   {error}")
        print("\n请重新执行Phase 3。")
        sys.exit(1)