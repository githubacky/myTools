# 作業dir内のhtmlファイル一覧を作成する。
# 汎用性を持たせるため、拡張子を変数とした。
import glob, subprocess
flname = "./target_html.txt"
ext = ".html"
target = glob.glob("src_html/*" + ext)
with open(flname, "w") as f:
	for t in target:
		tt = t.replace("./", "")
		tt = tt.replace(ext, "")
		f.write(tt + "\n")
#subprocess.call(["cat", flname]) # for Debug
