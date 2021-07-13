package STEP04

import java.util.*
import kotlin.collections.ArrayList


// https://cote.inflearn.com/contest/10/problem/04-01
// 가장많은 표를 받은 회장 알파벳 출력
/*
in
15
BACBACCACCBDEDE

out
C
*/

private fun solution(n: Int, s: String): String {
    var answer = ""
    val strList = s.toList()
    val maxTarget = strList.groupingBy { it }.eachCount().maxBy { it.value }?.component1() // component1 = 첫번째 값
    // println(strList) // [B, A, C, B, A, C, C, A, C, C, B, D, E, D, E]
    // println(maxTarget) // C

    return maxTarget.toString()
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val str = kb.next()
    println(solution(n, str))
}