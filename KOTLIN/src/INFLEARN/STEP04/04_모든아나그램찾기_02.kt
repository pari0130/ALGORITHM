package INFLEARN.STEP04

import java.util.*

// https://cote.inflearn.com/contest/10/problem/04-04
// 문자열 중 찾아야 하는 문자열에 해당 하는 값 구하기
// -> 출력설명: {bac}, {acb}, {cba} 3개의 부분문자열이 "abc"문자열과 아나그램입니다.
/*
in
bacaAacba
abc
bBacwgDwacBwxcaB
acB

out
3
*/
private fun solution(a: String, b: String): Int {
    var answer = 0
    a.toList().windowed(b.length).forEach {
        println(it.toHashSet().toList())
        if (it.toHashSet().toList() == b.toList()){
            answer++
        }
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val a = kb.next() // bacaAacba
    val b = kb.next() // abc
    print(solution(a, b))
}