package STEP01

import java.lang.StringBuilder
import java.util.Scanner

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n: Int = kb.nextInt()
    val str = ArrayList<String>()

    for (i in 1..n) {
        str.add(kb.next())
    }

    for (x in solution(n, str)) {
        println(x)
    }
}

private fun solution(n: Int, str: ArrayList<String>): ArrayList<String> {
    val answer = ArrayList<String>()

    for (x in str) {
        val s = x.toCharArray()
        var lt = 0
        var rt = x.length - 1
        while (lt < rt) {
            val tmp = s[lt]
            s[lt] = s[rt]
            s[rt] = tmp
            lt++
            rt--
        }
        val tmp = java.lang.String.valueOf(s)
        answer.add(tmp)
    }

    return answer
}
