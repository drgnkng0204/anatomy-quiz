# Firebase の設定手順(クラウド同期用)

1. https://console.firebase.google.com/ で「プロジェクトを追加」(Google アナリティクスは不要)
2. 左メニュー「ビルド」→「Firestore Database」→「データベースを作成」
   - ロケーション: asia-northeast1(東京)
   - モード: 本番環境モード
3. 「ルール」タブに `firestore.rules` の中身を貼り付けて「公開」
4. 歯車 →「プロジェクトの設定」→「全般」→「マイアプリ」→ ウェブ(`</>`)でアプリを登録
   - 表示される `firebaseConfig` のうち `apiKey` と `projectId` を `cloud.json` に書く
5. (推奨)Google Cloud Console →「API とサービス」→「認証情報」で、その API キーを
   - アプリケーションの制限: HTTP リファラー `https://drgnkng0204.github.io/*`
   - API の制限: Cloud Firestore API
