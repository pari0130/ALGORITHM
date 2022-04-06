package INFLEARN.STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-04
// 연속 부분수열의 합이 m 이 되는 경우가 몇번인지 구하기
/*
in
8 6
1 2 1 3 1 1 1 2

out
3
*/

private fun solution(n: Int, m: Int, arr: IntArray): Int {
    var answer = 0
    var sum = 0
    var lt = 0
    for (rt in 0 until n) {
        sum += arr[rt]
        if (sum == m) answer++
        while (sum >= m) {
            sum -= arr[lt++]
            if (sum == m) answer++
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt() // 10
    val m = kb.nextInt() // 3
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = kb.nextInt()
    }
    println(solution(n, m, arr))
}