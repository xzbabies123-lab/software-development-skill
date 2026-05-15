#!/usr/bin/env python3
"""
Phase 1验证脚本 - 验证UI设计稿是否生成
"""

import sys
import os

def validate_phase1_output(output_dir="/tmp"):
    """验证Phase 1输出是否符合规范"""
    
    errors = []
    
    # 检查1：是否有UI截图文件
    ui_files = [f for f in os.listdir(output_dir) if f.startswith('ui_') and f.endswith('.png')]
    if len(ui_files) == 0:
        errors.append("❌ 违规：未生成UI截图文件")
    
    # 检查2：是否有页面流程图
    flow_files = [f for f in os.listdir(output_dir) if 'flow' in f.lower() and f.endswith(('.png', '.md', '.txt'))]
    if len(flow_files) == 0:
        errors.append("❌ 违规：未生成页面流程图")
    
    if errors:
        return {"valid": False, "errors": errors}
    else:
        return {"valid": True, "ui_files": ui_files, "flow_files": flow_files}

if __name__ == "__main__":
    print("【Phase 1验证】")
    
    result = validate_phase1_output()
    
    if result["valid"]:
        print("\n✅ Phase 1验证通过")
        print(f"   UI截图：{len(result['ui_files'])}个")
        print(f"   流程图：{len(result['flow_files'])}个")
        sys.exit(0)
    else:
        print("\n❌ Phase 1验证失败：")
        for error in result["errors"]:
            print(f"   {error}")
        print("\n请重新执行Phase 1。")
        sys.exit(1)