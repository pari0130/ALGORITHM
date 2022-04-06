package INFLEARN.STEP04

import java.util.*


// https://cote.inflearn.com/contest/10/problem/04-03
// 중복되는 매출 제외한 연속된 <4 길이의 매출액 종류
/*
in
7 4
20 12 20 10 23 17 10

out
3 4 4 3
*/
private fun solution(n: Int, k: Int, arr: IntArray): ArrayList<Int> {
    val answer = ArrayList<Int>()
    val HM = HashMap<Int, Int>()
    for (i in 0 until k - 1) {
        HM[arr[i]] = HM.getOrDefault(arr[i], 0) + 1
    }
    var lt = 0
    for (rt in k - 1 until n) {
        HM[arr[rt]] = HM.getOrDefault(arr[rt], 0) + 1
        answer.add(HM.size)
        HM[arr[lt]] = HM[arr[lt]]!! - 1
        if (HM[arr[lt]] == 0) HM.remove(arr[lt])
        lt++
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
    for (x in solution(n, k, arr)) print("$x ")
}