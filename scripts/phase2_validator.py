#!/usr/bin/env python3
"""
Phase 2验证脚本 - 验证技术设计文档是否完整
"""

import sys
import os

def validate_phase2_output(output_dir="/tmp"):
    """验证Phase 2输出是否符合规范"""
    
    errors = []
    
    # 检查1：是否有数据库设计文件
    db_files = [f for f in os.listdir(output_dir) if 'database' in f.lower() or 'schema' in f.lower()]
    if len(db_files) == 0:
        errors.append("❌ 违规：未生成数据库设计文件")
    
    # 检查2：是否有API文档
    api_files = [f for f in os.listdir(output_dir) if 'api' in f.lower()]
    if len(api_files) == 0:
        errors.append("❌ 违规：未生成API文档")
    
    # 检查3：是否有CREATE TABLE语句
    design_doc = ""
    for f in db_files + api_files:
        try:
            with open(os.path.join(output_dir, f), 'r') as file:
                design_doc += file.read()
        except:
            pass
    
    if "CREATE TABLE" not in design_doc.upper():
        errors.append("❌ 违规：数据库设计缺少CREATE TABLE语句")
    
    if errors:
        return {"valid": False, "errors": errors}
    else:
        return {"valid": True, "db_files": db_files, "api_files": api_files}

if __name__ == "__main__":
    print("【Phase 2验证】")
    
    result = validate_phase2_output()
    
    if result["valid"]:
        print("\n✅ Phase 2验证通过")
        print(f"   数据库文件：{len(result['db_files'])}个")
        print(f"   API文档：{len(result['api_files'])}个")
        sys.exit(0)
    else:
        print("\n❌ Phase 2验证失败：")
        for error in result["errors"]:
            print(f"   {error}")
        print("\n请重新执行Phase 2。")
        sys.exit(1)