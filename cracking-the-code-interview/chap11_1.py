# What was the mistake?

"""
unsigned int i;
for (i = 100; i>=0;--i){
    printf("%d\n", i);
}

1. unsigned int 型だが、for文による繰り返しの最後にはi = -1になるため、エラーもしくは意図しない値になる
➝100~0までの表示をしたいならint型にするなど
2. unsigned int の表示時は、%uを使用する。
"""
