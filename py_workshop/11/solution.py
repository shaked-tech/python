def main(status,description):
  status_dict = {
    200:"OK",
    404:"Not Found",
    500:"Internal Server Error"
  }

  return {"statusCode":status, "statusText":status_dict[status],"data":description}


print(main(500, "hi im testing"))