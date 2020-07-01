"""
チェスの各駒クラスのメソッドであるcanMoveTO(int x , int y)のテスト方法を考えよう

動作の想定

入力
負の値や盤面の範囲外の値の入力➝False
盤面の範囲内かつ移動できるとき➝True
移動できない➝False

移動先に自駒➝FAlse
的駒➝True

優先順位
極端な入力よりも各駒の移動について検証する方が大事そう
"""

for peace in ["King", "Jack", "Queen", "Pool"]:  # 駒クラスとする
    for enemy in ["King", "Jack", "Queen", "Pool", None]:  # 駒クラス + 空欄とする
        for dvec in peace.dvecs:
            if enemy is not None:
                enemy.pos = dvec

            assert(peace.canMoneTo(dvec.x, dvec.y))
