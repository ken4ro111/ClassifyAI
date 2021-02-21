# アプリ使用方法
* git clone
```
git clone https://github.com/ken4ro111/ClassifyAI.git
```
* XCodeで開く
* ./ClassifyAI/swift_model/ClassfyAI/下に `train.mlmodel`を配置
    * [train_model](https://github.com/ken4ro111/ClassifyAI/tree/master/train_model)で学習済みの重みを、train_modelディレクトリ下の`convert.py`を使用して、.mlmodelに変換(`train.h5 => train.mlmodel`)し、`./ClassifyAI/ClassfyAI/下`に配置する
```
guard let model = try? VNCoreMLModel(for: model_name().model) else {
```
* XCodeでbuildする
