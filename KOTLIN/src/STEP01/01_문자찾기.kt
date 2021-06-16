package STEP01

import java.util.Scanner

// https://cote.inflearn.com/contest/10/problem/01-01

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str : String = kb.next()
    val c : Char = kb.next().single()

    println(solution(str, c))
    // val name = sc.nextLine()
    // val age = sc.nextInt()
}

private fun solution(str: String, t: Char): Int {
    var answer = 0

    str.toUpperCase().forEach {
        // println(it)
        if(it == t.toUpperCase()){
            answer++
        }
    }

    return answer
}
