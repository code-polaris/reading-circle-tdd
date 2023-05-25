# ReadingCircle_TDD

これは、CodePolaris のコミュニティ内で「テスト駆動開発」の輪読会を進めていく為のrepositoryです
https://amzn.asia/d/eOKrQ5s


# 輪読会の進め方
- 月1回、基本的に全員集まってdisucussionしたり、コードの見せあいをする(retrospective的な感じかと)
    - 詳しい日程は、CodePolaris内のディスコードイベントを要確認
- 章ごとに区切って、章/月で各自好きな言語で進めていく
    - 開発ペースは、別途のgit Issueを確認
      ﻿- 月一回の集まりの他に、毎週木曜21:00-はイベントをオープンにするけど、必須ではない
    - 進捗状況の共有とか喋りたいことがある人だけ集まりましょう
    - コード書かなくてものぞきに来るとかでもヨシ
    - 途中参加ももちろんオッケー！


# 開発構築
## GitHubのrepo/branch（main/自分の名前のbranchを各自作る）を作る
初めに、自分のローカル環境にgitがインストールされていることを確認して下さい
参考
https://www.sejuku.net/blog/73444

1. github内で新しいブランチを切る
   switch branches/tags -> View all Branches -> New branch
   Branch name： あなたの名前
   Branch source: main

    (ブランチをローカルで切ってからpushする方法もあるが、先にこれをしておいた方がラクチンです)
    先にレポジトリーをcloneしてしまった場合、上記の手順の後にローカルで git fetch -p　を呼ぶといいです。


2. レポジトリーをcloneする
`git clone ....`


3. ブランチを切り替える
`git checkout ...`


4. 【超大事】.gitignoreの編集
   [.gitignore](.gitignore) に、ビルドファイル(=コミットする必要のない余計なファイル)の情報を付け足す
   - python, Java, C#の分は足してありますので、特に他の言語を選んだ方はこれを編集するのを忘れずに行って下さい
   - これを忘れると、うっかりあなたの個人情報などの大事な情報をコミットしてしまう場合がありますので注意してください


# コミットのお作法 (gitBashなどを使う場合)
1. ステータス確認
   `git status`
   次に行うgit add をする前に必ずこれをやる癖をつけておくといいです。不必要なファイルをコミットしそうになってしまったら、そのファイルを.gitignoreに記載して除外するようにします


2. ステージング
   `git add .` （git statusで赤く表示されたファイルを全てコミットに含める）
   もしくは
   `git add <file name>`　（指定されたファイルのみをコミットに含める）


3. もう一度ステータス確認
`git status`
色が緑色に変わったファイルがstaging されたファイル
これらをコミットするかもう一度よく考える


5. コミットする
   `git commit -m "...."`
   ...の中にはメッセージを入れる
   issueナンバー + 過去形の動詞から始まる文 を入れるのが一般的だが、そこは自由でいいと思います
   (例：　"#10　Added logic for the reconcilliation")


6. 最後にもう一度ステータス確認(しつこい！)</br>
`git status`をする


7. コードをサーバーにプッシュする</br>
`git push`


### トラブルシューティング
#### ステージング
##### 特定のファイルやフォルダを除外したい場合
`git reset HEAD -- <file>` や `git reset HEAD -- <directoryName>`

##### 全てを除外して最初からやり直したい場合
`git reset`

# issue
issue はcommitに紐づく疑問点や問題点
issueナンバーをコミットメッセージに含めるのはチームプロジェクトの基本なので、是非やってみてね

TBC

# discussion
継続的に更新していくknowledge stackの更新

TBC