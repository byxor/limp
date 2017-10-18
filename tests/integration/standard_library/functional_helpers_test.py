import tests.helpers as Helpers


def test():
    Helpers.run_evaluation_test_on([
        ('((curry + 10) 20)',     30),
        ('((curry + 10 1 2) 20)', 33),
        ('((curry map (function (n) (* n 2))) (list 1 2 3))', [2, 4, 6]),
        ('((curry filter (function (n) (= n 1))) (list 1 2 3))', [1]),
        
        ("""
         (chain 0
           (function (n) (+ n 10))
           (function (n) (// n 2)))
         """, 5),

        ("""
         (chain (list 1 2 3 4 5 6 7 8 9 10)
           (curry map    (function (n) (* n 2)))
           (curry map    (function (n) (+ n 1)))
           (curry map    (function (n) (- n 1)))
           (curry filter (function (n) (= (% n 4) 0)))
           (curry reduce +))
         """, 60),
    ])
