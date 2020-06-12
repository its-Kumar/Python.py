def almost_there(num):
    return (
        (abs(num-100) <= 10) or (abs(num-200) <= 10)
    )


print(
    almost_there(102),
    almost_there(150),
    almost_there(198)

)
