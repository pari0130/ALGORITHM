package STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-03
// 매출 리스트에서 연속된 3일의 최대 매출 구하기
/*
in
10 3
12 15 11 20 25 10 20 19 13 15

out
56
*/
private fun solution(n: Int, k: Int, arr: IntArray): Int {
    var answer = 0
    var sum = 0
    for(i in 0 until k){
        sum += arr[i]
    }
    for(i in k until n){
        sum += (arr[i] -arr[i-k])
        answer = answer.coerceAtLeast(sum)
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt() // 10
    val k = kb.nextInt() // 3
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = kb.nextInt()
    }
    println(solution(n, k, arr))
}