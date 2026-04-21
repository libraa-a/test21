class StringUtils:
    """
    模拟 Apache Commons Lang 库中的 StringUtils 工具类
    """
    
    @staticmethod
    def reverse(s: str) -> str:
        """
        反转字符串
        """
        if s is None:
            return None
        return s[::-1]

    @staticmethod
    def capitalize(s: str) -> str:
        """
        将字符串的第一个字母转换为大写。
        
        【缺陷注入警告】：这里被故意注入了一个逻辑缺陷，
        原本应该使用 s[0].upper()，但故意改为了 s[0].lower()
        """
        if not s:
            return s
        # 软件缺陷类型：Logic Error (逻辑错误)
        return s[0].lower() + s[1:]
