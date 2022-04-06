package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 회문 문자열 비교, 문자열을 뒤집어도 같은지 체크 함
// teet : yes, test : no
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = "no"
    val tmp = StringBuilder(str).reverse().toString() // revers 를 이용하는 방법

    // 대소문자 구분없이 비교 : equals("string", ignoreCase = true)
    if(str.equals(tmp, ignoreCase = true)){
        answer = "yes"
    }

    return answer
}