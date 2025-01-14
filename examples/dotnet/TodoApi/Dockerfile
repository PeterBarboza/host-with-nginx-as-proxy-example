FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /App

COPY . ./

# Restore as distinct layers
RUN dotnet restore

# Build and publish a release
RUN dotnet publish -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/sdk:8.0

WORKDIR /App

COPY --from=build /App/out .

CMD ["dotnet", "TodoApi.dll"]
# ENTRYPOINT ["dotnet", "DotNet.Docker.dll"]