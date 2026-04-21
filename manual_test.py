from string_utils import StringUtils

def main():
    print("--- 开始运行不依赖工具的手工测试 ---")
    
    # 测试关键方法 1：reverse
    print("\n[测试] StringUtils.reverse()")
    res_rev = StringUtils.reverse("hello")
    if res_rev == "olleh":
        print(" -> [通过/PASS] 'hello' 成功反转为 'olleh'")
    else:
        print(f" -> [失败/FAIL] 期望: 'olleh', 实际: '{res_rev}'")
        
    # 测试关键方法 2：capitalize (包含注入缺陷的方法)
    print("\n[测试] StringUtils.capitalize()")
    res_cap = StringUtils.capitalize("hello")
    if res_cap == "Hello":
        print(" -> [通过/PASS] 'hello' 成功大写化为 'Hello'")
    else:
        print(f" -> [失败/FAIL] 期望: 'Hello', 实际: '{res_cap}'")
        
    print("\n--- 手工测试结束 ---")

if __name__ == "__main__":
    main()
