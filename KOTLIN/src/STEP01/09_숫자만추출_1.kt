package STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 문자열에서 숫자만 추출하여 숫자 조합의 값을 return
// dwe0dqwd2dwow0dw8 : 208
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}

private fun solution(str: String): Int {
    var answer = ""

    // string 을 하나씩 접근하여 숫자 일 경우 문자열에 더해준뒤 int return
    str.forEach {
        if(Character.isDigit(it)){
            answer += it
        }
    }

    return answer.toInt()
}