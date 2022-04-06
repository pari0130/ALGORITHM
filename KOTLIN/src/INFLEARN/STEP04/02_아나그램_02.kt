package INFLEARN.STEP04

import java.util.*
import kotlin.collections.ArrayList


// https://cote.inflearn.com/contest/10/problem/04-02
// 두 단어의 구성이 같으면 yes (a 가 2개 b가 2개 등등..)
/*
in
AbaAeCedas
baeeACAddd

out
YES
*/

private fun solution(s1: String, s2: String): String {
    var answer = "NO"
    val map1 = s1.toList().groupingBy { it }.eachCount()
    val map2 = s2.toList().groupingBy { it }.eachCount()

    println("$map1 ||| $map2")

    if(map1 == map2) {
        answer = "YES"
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val a = kb.next()
    val b = kb.next()
    print(solution(a, b))
}