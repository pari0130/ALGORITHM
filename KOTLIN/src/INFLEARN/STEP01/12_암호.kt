package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 4
// #****###**#####**#####**##**
// COOL
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n = kb.nextInt()
    val str = kb.next()
    println(solution(n, str))

}

private fun solution(n : Int, str: String): String {
    var answer = ""
    var s = str

    // 0..n-1 -> 0 until n
    for(i in 0 until n){
        val tmp = s.substring(0, 7).replace("#", "1").replace("*", "0")
        val num = Integer.parseInt(tmp, 2) // 10진수 to 2진수
        answer += num.toChar() // 2진수 아스키 코드 to 문자
        println("$tmp $num")
        s = s.substring(7)
    }

    return answer
}