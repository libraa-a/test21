.PHONY: test build

# test 目标：用来对程序进行冒烟测试
test:
    python -m unittest test_string_utils.py

# build 目标：模拟 Java 导出 jar 包的过程，这里我们把代码打包成 zip 分发包
build:
    python -m zipfile -c string_utils_app.zip string_utils.py
    @echo "打包完成，已生成 string_utils_app.zip"