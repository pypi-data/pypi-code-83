# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Wellcome to boke QA')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    def wait_for_appearance_click(self, timeout=60):
        """
        自定义方法:指定时间内没有出现该UI输出日志，否则点击该UI
        """

        start = time.time()
        while not self.exists():
            self.poco.sleep_for_polling_interval()
            if time.time() - start > timeout:
                log("没有等到该UI出现："+str(self))
                break
        else:
            self.click()

    def wait_for_appearance_continue(self,timeout=60):
        """
        自定义方法：指定时间内没出现该UI输出日志并继续，出现了则继续
        """

        start = time.time()
        while not self.exists():
            self.poco.sleep_for_polling_interval()
            if time.time() - start > timeout:
                log("没有等到该UI出现："+str(self))
                break  

    