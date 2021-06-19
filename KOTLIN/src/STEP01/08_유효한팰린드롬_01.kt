package STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 앞에서 읽을 때나 뒤에서 읽을 때나 같은 문자열을 팰린드롬이라고 합니다.
// 문자열에 대해서만 앞뒤가 같은지 비교하여 return
// found7, time: study; Yduts; emit, 7Dnuof >> yes
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.nextLine()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = "no"

    // kotlin 에서는 replaceAll 이 없기 때문에 toRegex() 로 담긴 변수를 이용하여 replace(reg, "") 해야 함함
    val re = "[^A-Z]".toRegex()
    val s = str.toUpperCase().replace(re, "")
    val tmp = StringBuilder(s).reverse().toString()

    if (s.equals(tmp)) {
        answer = "yes"
    }

    return answer
}