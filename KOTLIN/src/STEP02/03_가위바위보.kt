package STEP02

import java.lang.StringBuilder
import java.util.Scanner

// https://cote.inflearn.com/contest/10/problem/02-03
/*
    in
    5
    2 3 3 1 3
    1 1 2 2 3

    out
    A B A B D
*/
private fun solution(n: Int, a: IntArray, b: IntArray): String {
    val answer = StringBuilder()

    a.forEachIndexed { index, value ->
        if (value == b[index]) {
            answer.append("D ")
        } else if (value == 1 && b[index] == 3) {
            answer.append("A ")
        } else if (value == 2 && b[index] == 1) {
            answer.append("A ")
        } else if (value == 3 && b[index] == 2) {
            answer.append("A ")
        } else {
            answer.append("B ")
        }
    }

    return answer.toString()
}

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n = kb.nextInt()
    val a = IntArray(n)
    val b = IntArray(n)

    for (i in 0 until n) {
        a[i] = kb.nextInt()
    }
    for (i in 0 until n) {
        b[i] = kb.nextInt()
    }

    println(solution(n, a, b))
}