import pandas as pd
import os
import time

def open_links_in_safari_private(csv_path):
    # 读取CSV文件
    df = pd.read_csv(csv_path)

    # 确保CSV文件中有一个名为'links'的列
    if 'links' not in df.columns:
        print("CSV文件中没有名为'links'的列，请检查您的文件。")
        return

    # 使用AppleScript在Safari无痕浏览窗口中打开链接
    applescript = '''
    on openURLInPrivateTab(theURL)
        tell application "Safari"
            activate
            tell application "System Events"
                tell process "Safari"
                    keystroke "t" using command down
                end tell
            end tell
            set URL of document 1 to theURL
        end tell
    end openURLInPrivateTab
    '''

    # 首先打开一个无痕浏览窗口
    os.system("open -a Safari --args --private")

    for link in df['links']:
        os.system(f"osascript -e '{applescript}' -e 'openURLInPrivateTab(\"{link}\")'")
        time.sleep(0.1)  # 每个链接之间暂停0.1秒，以免过快打开过多标签页

if __name__ == "__main__":
    # 替换为您的CSV文件路径
    csv_path = 'url.csv'
    open_links_in_safari_private(csv_path)