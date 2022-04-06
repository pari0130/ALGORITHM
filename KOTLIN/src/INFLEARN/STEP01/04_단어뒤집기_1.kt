package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n : Int = kb.nextInt()
    val str = ArrayList<String>()

    for(i in 1..n){
        str.add(kb.next())
    }

    for(x in solution(n, str)){
        println(x)
    }
}

private fun solution(n: Int, str : ArrayList<String>) : ArrayList<String> {
    val answer = ArrayList<String>()

    for(x in str){
        val tmp = StringBuilder(x).reverse().toString()
        answer.add(tmp)
    }

    return answer
}
