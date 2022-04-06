package INFLEARN.STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-06
/*
    in
    9
    32 55 62 20 250 370 200 30 100

    out
    23 2 73 2 3
*/

private fun isPrime(num : Int) : Boolean {

    if(num == 1)
        return false

    for(i in 2 until num){
        if(num%2 == 0)
            return false
    }

    return true
}

private fun solution(n: Int, arr : IntArray): ArrayList<Int> {
    val answer = ArrayList<Int>()

    for(i in 0 until n){
        var tmp = arr[i]
        var res = 0

        while (tmp > 0){
            val t = tmp%10
            res = res*10+t
            tmp /= 10
        }

        if(isPrime(res))
            answer.add(res)
    }

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)

    for(i in 0 until n){
        arr[i] = kb.nextInt()
    }

    solution(n, arr).forEach{
        print("$it ")
    }
}