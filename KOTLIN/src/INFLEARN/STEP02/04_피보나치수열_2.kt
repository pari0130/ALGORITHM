package INFLEARN.STEP02

import java.lang.StringBuilder
import java.util.Scanner

// https://cote.inflearn.com/contest/10/problem/02-04
/*
    in
    10

    out
    1 1 2 3 5 8 13 21 34 55
*/
// list 를 사용하지 않는 방식
private fun solution(n: Int): String {
    val answer = StringBuilder()
    var a = 1
    var b = 1
    var c : Int
    answer.append("$a ").append("$b ")

    for(i in 2 until n){
        c = a + b
        answer.append("$c ")
        a = b
        b = c
    }

    return answer.toString()
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()

    println(solution(n))
}