# creating a request object

{

    "status": "pending",
    "amount": "0.00",
    "purpose": "buy",
    "reason": "cars",
    "type": "business",
    "memberId": "GIA-118940529911204028031"
}


# creating a user account
{
    "firstname": "Kelvin",
    "lastname": "Akoto Bamfo",
    "dob": "12th september",
    "gender": "male",
    "email": "ernest6175@gmail.com",
    "pin": "123412",
    "phoneNumber": "0255421892",
    "username": "crypto",
    "memberType": "student",
    "profileImage": "url",
    "documents":
    {
                "ghanaCardNumber": "GHA-1938391892381921-0",
                "frontCardPic": "kelvin",
                "backCardPic": "kelvin"
    }

}


# delete a request
{
    "requestId": "3232edbd-567e-435c-9f82-5890bfc07743"
}


# update user profile


{"memberId": "GIA-118940529911204028031",
    "firstname": "Kelvin",
    "lastname": "Akoto Bamfo",
    "dob": "12th september",
    "gender": "male",
    "memberType": "student",
    "profileImage": "url"
 }

# update user pin info
{"memberId": "GIA-118940529911204028031",
 "pin": "123-tes@"
 }

# update user email info
{"memberId": "GIA-118940529911204028031",
 "email": "test@gmail.com"
 }

# delete user
{"memberId": "GIA-118940529911204028031"
 }

# update user phone phoneNumber

{"memberId": "GIA-118940529911204028031",
 "phoneNumber": "0255421892"

 }


# update user documents
{"memberId": "GIA-118940529911204028031",
 "documents":
    {
        "ghanaCardNumber": "GHA-1938391892381921-0",
        "frontCardPic": "kelvin",
        "backCardPic": "kelvin"
    }

 }
