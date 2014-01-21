# unsynthesize

iosアプリ開発において、mファイルから@synthesizeを取り除き、それまでに@synthesizeされていたプロパティ変数名の先頭に"_"(アンダースコア)を挿入するツールです。self.barなど、ドット演算子でアクセスされている場合はそのままにしておきます。

#Usage

以下のように第一引数にファイル名を与えて下さい。

```shell
$ python unsynthesize.py foo.m
```

# 動機
昔はpublicな変数を使うために、以下のようなコードを書く事がよくありました。

```Foo.h
@interface Foo : NSObject
@property bar;
@end
```

```Foo.m
#import "Foo.h"

@implementation Foo
@synthesize bar;
@synthesize baz;
-(id)init:(int)val
{
    [super init];
    bar = val;
    self.baz = val * 2;
}
@end
```

しかし、現在では`@synthesize`をしなくても、.hファイルで

```Foo.h
@property bar;
```
の記載があれば、

```main.m
Foo * foo = [[Foo alloc] init:3];
NSLog(@"%d", foo.bar);
```
のように外からプロパティにアクセスできるようになりました。`@synthesize`文は冗長性があるので、個人的には使用したくないです。そこで、上記Foo.mを入力として受け取り、

```Foo.m
#import "Foo.h"

@implementation Foo
-(id)init:(int)val
{
    [super init];
    _bar = val;
    self.baz = val * 2;
}
@end
```
のように編集するツールを作成しました。

# 注意
現在、メソッド名や文字列中にsynthesizeされていた文字と同じものが入っていると、その部分も変更されてしまうバグがあります。それ以外はだいたいうまく行きます。

