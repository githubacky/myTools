# 作業dir内のhtmlファイル一覧を作成する。
import glob, subprocess
flname = "./target_html.txt"
target = glob.glob("./*.html")
with open(flname, "w") as f:
    for t in target:
        tt = t.replace("./", "")
        tt = tt.replace(".html", "")
        f.write(tt + "\n")
#subprocess.call(["cat", flname])
