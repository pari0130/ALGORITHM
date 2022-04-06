package INFLEARN.STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-06
// 0 1 로 구성된 숫자 리스트에서 0을 1로 k번 만 변경 후 연속되는 1의 최대 길이 구하기
/*
in
14 2
1 1 0 0 1 1 0 1 1 0 1 1 0 1

out
8
*/

private fun solution(n: Int, k: Int, arr: IntArray): Int {
    var answer = 0
    var cnt = 0
    var lt = 0
    for (rt in 0 until n) {
        if (arr[rt] == 0) cnt++
        while (cnt > k) {
            if (arr[lt] == 0) cnt--
            lt++
        }
        answer = Math.max(answer, rt - lt + 1)
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val k = kb.nextInt()
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = kb.nextInt()
    }
    print(solution(n, k, arr))
}