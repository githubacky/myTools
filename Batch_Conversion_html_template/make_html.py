'''
HTMLファイルテンプレート更新プログラム
2020/2/19 by Yuichiro Akimoto
Python version: 3.7.4
Revision:
	0.00	新規作成	2020/2/19
機能：
	複数HTMLファイルの共通部分を一括更新する。
	対象雛形ファイル"hoge.html"とテンプレートファイル"template.html"を合成し、
	更新後ファイル"hoge.html"を出力する。
ディレクトリ構成：
	対象雛形htmlファイル格納先：src_html
	更新後htmlファイル出力先：out_html
	template.htmlは本プログラムと同じ階層に置くこと。
'''

# テンプレートファイルのリスト化
src_dir = "src_html"
out_dir = "out_html"
tmpfl = "./template.html"
with open(tmpfl) as t:
	tmpli = t.readlines()

# 対象HTMLファイルのリスト化
target = open("./target_html.txt", "rt")
for t in target:
	if t[0] != "#":
		with open(t.strip() + ".html") as f:
			tgtli = f.readlines()

		# ファイル合成
		outli = []
		for idx, tmp in enumerate(tmpli):
			if "<!-- Start Target -->" in tmp:
				outli.append(tmp)
				for tg in tgtli:
					outli.append(tg)
			else:
				outli.append(tmp)

		# 更新後HTMLファイル出力
		outfl = t.strip().replace(src_dir, out_dir) + ".html"
		with open(outfl, mode="w") as o:
			o.write("".join(outli))
target.close()
