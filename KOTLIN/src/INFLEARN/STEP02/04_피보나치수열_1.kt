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
private fun solution(n: Int): IntArray {
    val answer = IntArray(n)
    answer[0] = 1
    answer[1] = 1

    for (i in 2 until n) {
        answer[i] = answer[i - 2] + answer[i - 1]
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()

    solution(n).forEach {
        print("$it ")
    }
}