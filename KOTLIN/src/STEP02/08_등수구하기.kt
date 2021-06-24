package STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-08
// 점수가 높은 사람이 나오면 등수를 +1
/*
    in
    5
    87 89 92 100 76

    out
    4 3 2 1 5
*/
private fun solution(n: Int, arr: IntArray): IntArray {
    val answer = IntArray(n)
    for (i in 0 until n) {
        var cnt = 1
        for (j in 0 until n) {
            if (arr[j] > arr[i]) cnt++
        }
        answer[i] = cnt
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)

    for (i in 0 until n) {
        arr[i] = kb.nextInt()
    }

    solution(n, arr).forEach {
        print("$it ")
    }
}