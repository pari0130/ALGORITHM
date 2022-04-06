package INFLEARN.STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-09
// 격자판 가로, 세로, 대각선의 합 중 가장 높은 값 구하기
/*
    in
    5
    10 13 10 12 15
    12 39 30 23 11
    11 25 50 53 15
    19 27 29 37 27
    19 13 30 13 19

    out
    155
*/
private fun solution(n: Int, arr: Array<IntArray>): Int {
    var answer = -2147000000
    var sum1 = 0
    var sum2 = 0
    for (i in 0 until n) {
        sum2 = 0
        sum1 = sum2
        for (j in 0 until n) {
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        }
        //#팀 큰수 비교 Math.max(a,b) answer 과 sum 중 큰 값을 찾기 위한 식
        answer = answer.coerceAtLeast(sum1)
        answer = answer.coerceAtLeast(sum2)
    }
    sum2 = 0
    sum1 = sum2
    for (i in 0 until n) {
        sum1 += arr[i][i]
        sum2 += arr[i][n - i - 1]
    }
    answer = answer.coerceAtLeast(sum1)
    answer = answer.coerceAtLeast(sum2)
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = Array(n) { IntArray(n) }
    for (i in 0 until n) {
        for (j in 0 until n) {
            arr[i][j] = kb.nextInt()
        }
    }
    print(solution(n, arr))
}