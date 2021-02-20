# 使用方法
Python 3.8.
```
pip install -r requirements.txt
```

### 学習
* `./train_model/`下にdirを作成
```
mkdir train_data
mkdir val_data
```

* train_data、val_data内に学習する画像をclass事にディレクトリに分けて配置する
* 例
```
train_data - dog
           |
           |- cat
           |
           |- monkey

val_data - dog
           |
           |- cat
           |
           |- monkey
```

* 学習: model.py
    * 使用されるmodelはデフォルトでは`VGG16`になっている
        * model.pyの[69行目](https://github.com/ken4ro111/ClassifyAI/blob/master/train_model/model.py#L69)で変更可能

* 学習: model.py
```
Python model.py
```

* train_weights.h5が生成される

### train_weights.h5をswiftで使用できる様に変換
**.h5 => **.mlmodelへ変換する
* convert.py
* labels.txtにtrain_data、val_dataに配置したclass名を記入する
    * 例: lavels.txt
```
dog
cat
monkey
```

```
Python convert.py
```

* train.mlmodelが生成される
* ClassifyAI/swift_model/ClassifyAI/下に`train.mlmodel`を配置する
