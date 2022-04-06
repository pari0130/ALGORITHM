package INFLEARN.STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-11
// 반장이었던 학생 번호가 주어지고, 각 학년을 지나오면서 가장많은 학생들과 겹처있을 경우 임시반장 번호 출력
/*
in
5
2 3 1 7 3
4 1 9 6 8
5 5 2 4 4
6 5 2 6 7
8 4 2 2 2

out
4
*/
private fun solution(n: Int, arr: Array<IntArray>): Int {
    var answer = 0
    var max = Integer.MIN_VALUE
    // 현재 학생 i
    for (i in 1..n) {
        var cnt = 0
        // 현재 학생의 학년 loop
        for (j in 1..n) {
            // 현재 학생과 동일한 학년에 속해 있던 반장출신 5명
            for (k in 1..5) {
                if (arr[i][k] == arr[j][k]) {
                    cnt++
                    break
                }
            }
        }
        if (cnt > max) {
            max = cnt
            answer = i
        }
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = Array(n + 1) { IntArray(6) }
    for (i in 1..n) {
        for (j in 1..n) {
            arr[i][j] = kb.nextInt()
        }
    }
    print(solution(n, arr))
}