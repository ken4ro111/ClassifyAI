# アプリ使用方法
* git clone
```
git clone https://github.com/ken4ro111/ClassifyAI.git
```
* XCodeで開く
* ./ClassifyAI/swift_model/ClassfyAI/**.mlmodelを配置
    * 学習済みの重みを.mlmodelに変換(**.mlmodel)し、./ClassifyAI/ClassfyAI/下にドラッグ・アンド・ドロップ
* **.mlmodel配置後、`ViewController.swift`の下記の行を修正
    * `model_name().model`の`model_name()`の部分を`**.mlmodel`の`**`部分に変更
    * 例: `train.mlmodel` => `train()`
```
guard let model = try? VNCoreMLModel(for: model_name().model) else {
```
* build
